from django.urls import path
from . import views

urlpatterns = [
    path('', views.django_index, name='index'),
    path('login/', views.django_login, name='login'),
    path('register/', views.django_register, name='register'),
    path('about_Us/', views.django_about, name='about-us'),
    path('activities/', views.django_activities, name='activities'),
    path('gallery/', views.django_gallery, name='gallery'),
    path('contact_us/', views.django_contact, name='contact-us'),
    path('request/', views.django_request, name='request'),
]