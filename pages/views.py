from django.shortcuts import render
from blog.models import Post
from django.http import JsonResponse, HttpResponse
from accounts.models import NewsletterUser

def home_view(request):
    # Zakomentuj to na chwilę:
    # posts = Post.objects.all()
    # return render(request, 'pages/home.html', {'posts': posts})
    
    # Zwróć prosty tekst:
    return HttpResponse("Strona działa, teraz naprawiamy bazę!")

def naxiom_view(request):
    return render(request, 'pages/naxiom.html')


def newsletter_signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            # Sprawdzamy, czy e-mail już istnieje, żeby nie dublować
            obj, created = NewsletterUser.objects.get_or_create(email=email)
            if created:
                return JsonResponse({'status': 'success', 'message': 'Dziękujemy za zapis!'})
            else:
                return JsonResponse({'status': 'info', 'message': 'Ten e-mail jest już w naszej bazie.'})
    return JsonResponse({'status': 'error', 'message': 'Coś poszło nie tak.'}, status=400)