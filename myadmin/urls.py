from django.urls import path
from . import views

urlpatterns = [
    path('', views.django_admin_panel, name='login'),
    path('Dashboard', views.django_admin_dashboard, name='admindashboard'),
]