from django.shortcuts import render

# Create your views here.
def django_login(request):
     return render(request,'view/login.html')

def django_register(request):
     return render(request,'view/register.html')

def django_index(request):
     return render(request,'view/index.html')

def django_about(request):
     return render(request,'view/about-us.html')

def django_activities(request):
     return render(request,'view/activities.html')

def django_projects(request):
     return render(request,'view/projects.html')

def django_gallery(request):
     return render(request,'view/gallery.html')

def django_contact(request):
     return render(request,'view/contact.html')

def django_request(request):
     return render(request,'view/request.html')

