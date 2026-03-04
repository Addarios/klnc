from django.shortcuts import render
from blog.models import Post
from django.http import JsonResponse, HttpResponse
from accounts.models import NewsletterUser
from django.db import connection

def home_view(request):
    # Sprawdzamy, czy tabela blog_post w ogóle istnieje w bazie danych
    all_tables = connection.introspection.table_names()
    
    if "blog_post" in all_tables:
        from blog.models import Post
        posts = Post.objects.all()
        return render(request, 'pages/home.html', {'posts': posts})
    else:
        return HttpResponse("Serwer działa, ale tabela 'blog_post' wciąż nie powstała w PostgreSQL.")

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


# pages/views.py
from django.contrib.auth.models import User
from django.http import HttpResponse

def check_admin(request):
    admins = User.objects.filter(is_superuser=True)
    if admins.exists():
        admin_list = ", ".join([u.username for u in admins])
        return HttpResponse(f"Znaleziono superadministratorów: {admin_list}")
    return HttpResponse("Brak superużytkowników w bazie danych!")