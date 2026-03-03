from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Lesson, Module, UserLessonProgress


@login_required
def course_list(request):
    # Pobieramy wszystkie moduły i "doczepiamy" do nich lekcje
    modules = Module.objects.all().prefetch_related('lessons').order_by('order')
    return render(request, 'courses/course_list.html', {'modules': modules})

@login_required
def lesson_detail(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)
    modules = Module.objects.all().prefetch_related('lessons')
    
    # Pobieramy ID ukończonych lekcji dla zalogowanego użytkownika
    completed_lessons_ids = UserLessonProgress.objects.filter(
        user=request.user
    ).values_list('lesson_id', flat=True)
    
    # Sprawdzamy, czy BIEŻĄCA lekcja jest już ukończona (do ukrycia przycisku)
    is_completed = lesson.id in completed_lessons_ids

    return render(request, 'courses/lesson_detail.html', {
        'lesson': lesson,
        'modules': modules,
        'completed_lessons_ids': completed_lessons_ids,
        'is_completed': is_completed
    })


@login_required
def complete_lesson(request, slug):
    if request.method == 'POST': # Bezpieczniej jest obsługiwać to przez POST
        lesson = get_object_or_404(Lesson, slug=slug)
        UserLessonProgress.objects.get_or_create(user=request.user, lesson=lesson)
    return redirect('lesson_detail', slug=slug)

@login_required
def course_list(request):
    modules = Module.objects.all().prefetch_related('lessons')
    
    # Obliczanie postępu
    total_lessons = Lesson.objects.count()
    completed_lessons_ids = UserLessonProgress.objects.filter(user=request.user).values_list('lesson_id', flat=True)
    
    progress_percent = 0
    if total_lessons > 0:
        progress_percent = int((len(completed_lessons_ids) / total_lessons) * 100)
    
    return render(request, 'courses/course_list.html', {
        'modules': modules,
        'completed_lessons_ids': completed_lessons_ids,
        'progress_percent': progress_percent
    })