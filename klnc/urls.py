from django.contrib import admin
from django.urls import path,include
from pages.views import home_view, naxiom_view
from blog.views import blog_list, post_detail # Dodaj import post_detail
from contact.views import contact_view # Importuj widok kontaktu
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views # Import widoków auth
from courses.views import course_list, lesson_detail # Dodaj import
from courses import views as course_views # Importuje cały plik jako obiekt 'course_views'
from pages.views import newsletter_signup


def force_migrate(request):
    call_command('migrate', interactive=False)
    return HttpResponse("Migracja wykonana!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('blog/', blog_list, name='blog'),
    path('kontakt/', contact_view, name='contact'),
    path('blog/<int:pk>/', post_detail, name='post_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('summernote/', include('django_summernote.urls')),
    path('sql-kurs/', course_views.course_list, name='course_list'),
    path('sql-kurs/lekcja/<slug:slug>/', course_views.lesson_detail, name='lesson_detail'),
    path('sql-kurs/complete/<slug:slug>/', course_views.complete_lesson, name='complete_lesson'),
    path('oferta/naxiom/', naxiom_view, name='naxiom_page'),
    path('accounts/', include('accounts.urls')),
    path('newsletter-signup/', newsletter_signup, name='newsletter_signup'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)