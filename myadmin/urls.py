from django.urls import path
from .views import *

urlpatterns = [
    path('', django_admin_panel, name='alogin'),
    path('/Dashboard', django_admin_dashboard, name='admindashboard'),
    path('/alluser', django_admin_alluser, name='alluser'), 
    path('/Request', django_admin_request, name='request'), 
    path('/PasswordChange', django_admin_changepassword, name='changepassword'),    
]