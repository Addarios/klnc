from django.contrib import admin
from .models import NewsletterUser

@admin.register(NewsletterUser)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added')
    search_fields = ('email',)