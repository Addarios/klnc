from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'tag', 'author') # Dodaj 'tag' tutaj
    list_filter = ('tag', 'published_date') # Dodaj filtrowanie po tagu