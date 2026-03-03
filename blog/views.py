from django.shortcuts import render, get_object_or_404 # Poprawione tutaj
from .models import Post

def blog_list(request):
    tag_filter = request.GET.get('tag')
    
    if tag_filter:
        # Zmieniamy date_posted na published_date
        posts = Post.objects.filter(tag=tag_filter).order_by('-published_date')
    else:
        # Tutaj również zmiana
        posts = Post.objects.all().order_by('-published_date')
        
    return render(request, 'blog/blog_list.html', {'posts': posts, 'selected_tag': tag_filter})

def post_detail(request, pk):
    # Szukamy postu o danym ID, a jeśli go nie ma - zwracamy błąd 404
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def course_list(request):
    modules = Module.objects.all().prefetch_related('lessons')
    return render(request, 'courses/course_list.html', {'modules': modules})