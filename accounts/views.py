from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import NewsletterUser # Importujemy model newslettera
from django.contrib.auth import login # Dodaj ten import

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # 1. Zapisujemy użytkownika
            user = form.save()
            
            # 2. Sprawdzamy checkbox newslettera
            subscribe = form.cleaned_data.get('subscribe_newsletter')
            if subscribe:
                email = form.cleaned_data.get('email')
                # get_or_create zapobiegnie błędom, jeśli mail już był w bazie
                NewsletterUser.objects.get_or_create(email=email)
            
            login(request, user)

            messages.success(request, f'Witaj {user.username}! Twoje konto zostało stworzone i jesteś już zalogowany.')            
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})