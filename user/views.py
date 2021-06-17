from django.shortcuts import render
from .models import Contact
# Create your views here.
def django_login(request):
     return render(request,'view/login.html')

def django_register(request):
     return render(request,'view/register.html')

def django_index(request):
     context = {
          "img": ['gallery1', 'gallery2', 'gallery3', 'gallery4', 'gallery5', 'gallery6', 'gallery7', 'gallery8']
     }
     return render(request, 'view/index.html', context)

def django_about(request):
     return render(request, 'view/about-us.html')

def django_activities(request):
     context = {
          "daysOfWeek": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
     }
     return render(request, 'view/activities.html', context)

def django_gallery(request):
     context = {
          "img": ['gallery1', 'gallery2', 'gallery3', 'gallery4', 'gallery5', 'gallery6', 'gallery7', 'gallery8']
     }
     return render(request, 'view/gallery.html', context)

def django_contact(request):
     if request.method == 'POST':
         name = request.POST['name']
         email = request.POST['email']
         subject = request.POST['subject']
         message = request.POST['message']
         objContact = Contact()
         objContact.name = name
         objContact.email = email
         objContact.subject = subject
         objContact.message = message
         objContact.save()
     return render(request, 'view/contact.html')

def django_request(request):
     return render(request, 'view/request.html')

