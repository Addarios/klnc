from django.db import models
from django.conf import settings # Importujemy ustawienia, by mieć dostęp do modelu User


class Module(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nazwa modułu")
    order = models.IntegerField(default=0, verbose_name="Kolejność modułu")

    class Meta:
        ordering = ['order']
        verbose_name = "Moduł"
        verbose_name_plural = "Moduły"

    def __str__(self):
        return self.title

class Lesson(models.Model):
    module = models.ForeignKey(
        Module, 
        on_delete=models.CASCADE, 
        related_name='lessons', 
        verbose_name="Moduł",
        null=True,   # Pozwala bazie przechowywać NULL
        blank=True   # Pozwala formularzom w adminie zostawić to pole puste
        )   
    title = models.CharField(max_length=200, verbose_name="Tytuł lekcji")
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name="Treść lekcji")
    order = models.IntegerField(default=0, verbose_name="Kolejność w module")

    class Meta:
        ordering = ['order']
        verbose_name = "Lekcja"
        verbose_name_plural = "Lekcje"

    def __str__(self):
        return f"{self.module.title} - {self.title}"



class UserLessonProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'lesson') # Użytkownik może ukończyć daną lekcję tylko raz

    def __str__(self):
        return f"{self.user.username} ukończył {self.lesson.title}"