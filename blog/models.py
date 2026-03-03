from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, verbose_name="Obrazek")
    content = models.TextField(verbose_name="Treść")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="Data publikacji")
    author = models.CharField(max_length=100, verbose_name="Autor", default="Admin")

    TAG_CHOICES = [
        ('ogolne', 'Ogólne'),
        ('naxiom', 'nAxiom'),
        ('sql', 'SQL'),
    ]
    tag = models.CharField(max_length=20, choices=TAG_CHOICES, default='ogolne')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Wpis"
        verbose_name_plural = "Wpisy"


class NewsletterUser(models.Model):
    email = models.EmailField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email