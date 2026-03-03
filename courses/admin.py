from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Module, Lesson


@admin.register(Lesson)
class LessonAdmin(SummernoteModelAdmin): # Zmieniamy klasę bazową
    summernote_fields = ('content',)      # Wskazujemy pole tekstowe
    list_display = ('title', 'module', 'order')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Module)

