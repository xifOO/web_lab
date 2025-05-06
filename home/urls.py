from django.conf import settings
from .views import feedback_view, logout_user, registration, blog, watch_detail, add_watch
from django.views.generic import TemplateView
from django.urls import path
from django.contrib.auth import views
from django.conf.urls.static import static


urlpatterns = [
    path('', TemplateView.as_view(template_name="home/home.html"), name='home'),
    path('links', TemplateView.as_view(template_name="home/links.html"), name='links'),
    path('about', TemplateView.as_view(template_name="home/about.html"), name='about'),
    path('contacts', TemplateView.as_view(template_name="home/contacts.html"), name='contacts'),
    path('video', TemplateView.as_view(template_name="home/video.html"), name='video'),
    path('feedback/', feedback_view, name='feedback'),
    path('registration/', registration, name='registration'),
    path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', logout_user, name='logout'),
    path('blog/', blog, name='blog'),
    path('post/<int:parameter>/', watch_detail, name='post_detail'),
    path('add/', add_watch, name='add_watch'),
]
