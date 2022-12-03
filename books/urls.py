from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main_window, name='main_window'),
    path('registered/', views.registered, name='registered'),
    path('login/', auth_views.LoginView.as_view(template_name = 'books/login.html'), name = 'show_login'),
    path('register/', views.show_register, name='show_register'),
    path('logout/', views.logout_view, name='logout_view'),
    path('book/<int:arg>', views.show_book, name='show_book'),
    path('payment/', views.show_payment, name='show_payment'),
    path('return/', views.show_return, name='show_return'),
    path('add_comment/<int:arg>', views.add_comment, name='add_comment'),
    path('show_contacts/', views.show_contacts, name='show_contacts'),
    path('show_help/', views.show_help, name='show_help'),
    path('show_about/', views.show_about, name='show_about'),
    path('show_news/', views.show_news, name='show_news'),
    path('show_bestsellers/', views.show_bestsellers, name='show_bestsellers'),
    path('show_history/', views.show_history, name='show_history'),
    path('show_all/', views.show_all, name='show_all'),
    path('show_audio/', views.show_audio, name='show_audio'),
    path('show_experts/', views.show_experts, name='show_experts'),
    path('show_searched/', views.show_searched, name='show_searched'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)