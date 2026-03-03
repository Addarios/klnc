from django.shortcuts import render
from blog.models import Post
from django.http import JsonResponse
from accounts.models import NewsletterUser

def home_view(request):
    # Pobieramy 3 najnowsze posty
    latest_posts = Post.objects.all().order_by('-published_date')[:3]
    return render(request, 'pages/home.html', {'latest_posts': latest_posts})

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