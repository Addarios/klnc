from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import NewsletterUser # Importujemy model newslettera
from django.contrib.auth import login # Dodaj ten import
from django.db import transaction # Dodaj to!
from django.core.mail import send_mail


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                # Używamy atomic, żeby operacje na bazie były spójne
                with transaction.atomic():
                    user = form.save()
                    
                    # Logika newslettera
                    subscribe = form.cleaned_data.get('subscribe_newsletter')
                    if subscribe:
                        email = form.cleaned_data.get('email')
                        NewsletterUser.objects.get_or_create(email=email)
                
                # DOPIERO TUTAJ, poza blokiem atomic, wysyłamy maila
                # Jeśli mail zawiedzie, użytkownik i tak ma już konto
                send_welcome_email(user, form.cleaned_data.get('email'))
                
                login(request, user)
                messages.success(request, "Konto założone! Witaj na pokładzie.")
                return redirect('home')
                
            except Exception as e:
                # Jeśli coś pójdzie nie tak z bazą danych
                messages.error(request, "Wystąpił błąd podczas tworzenia konta. Spróbuj ponownie.")
                print(f"Błąd rejestracji: {e}")
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# Dobrą praktyką jest wydzielenie maila do osobnej funkcji
def send_welcome_email(user, user_email):
    subject = 'Witaj w Moja Platforma IT!'
    message = f'Cześć {user.username}, dziękujemy za rejestrację!'
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=True, # Bardzo ważne! Nie przerywaj działania strony, jeśli mail nie wyjdzie
        )
    except:
        pass # Logujemy błąd po cichu