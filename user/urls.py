from django.urls import path
from . import views

urlpatterns = [
    path('',views.django_index,name='index'),
    path('Login/',views.django_login,name='login'),
    path('Register/',views.django_register,name='register'),
    path('About_Us/',views.django_about,name='about-us'),
    path('Activities/',views.django_activities,name='activities'),
    path('Projects/',views.django_projects,name='projects'),
    path('Gallery/',views.django_gallery,name='gallery'),
    path('Contact_us/',views.django_contact,name='contact-us'),
    path('Request/', views.django_request, name='request'),
    
]