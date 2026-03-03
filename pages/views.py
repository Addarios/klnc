from django.shortcuts import render
from blog.models import Post

def home_view(request):
    # Pobieramy 3 najnowsze posty
    latest_posts = Post.objects.all().order_by('-published_date')[:3]
    return render(request, 'pages/home.html', {'latest_posts': latest_posts})

def naxiom_view(request):
    return render(request, 'pages/naxiom.html')