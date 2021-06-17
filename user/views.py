from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def django_login(request):
    if request.method == 'POST':
        try:
            uName = request.POST['email']
            uPwd = request.POST['pwd']
            uDetail = User.objects.get(email=uName, pwd=uPwd)
            if uDetail:
                request.session['user_id'] = uDetail.id
                return redirect('index')
        except ObjectDoesNotExist:
            return render(request, 'view/login.html', {"txtErr": "Please enter Valid EmailId Or Password"})
    else:
        return render(request, 'view/login.html')

def django_register(request):
     if request.method == 'POST':
         fName = request.POST['fName']
         lName = request.POST['lName']
         mono = request.POST['mono']
         gender = request.POST['gender']
         dob = request.POST['dob']
         bGrp = request.POST['bGrp']
         email = request.POST['email']
         state = request.POST['state']
         city = request.POST['city']
         area = request.POST['area']
         add = request.POST['add']
#        pincode = request.POST['pincode']
         pwd = request.POST['pwd']
         objUser = User()
         objUser.fName = fName
         objUser.lName = lName
         objUser.mono = mono
         objUser.gender = gender
         objUser.dob = dob
         objUser.bGrp = bGrp
         objUser.email = email
         objUser.state = state
         objUser.city = city
         objUser.area = area
         objUser.add = add
#        objUser.pincode = pincode
         objUser.pwd = pwd
         objUser.save()
         print(fName, lName, add, mono, email)
     return render(request, 'view/register.html')

def django_index(request):
     context = {
        "uId": getSession(request),
        "img": ['gallery1', 'gallery2', 'gallery3', 'gallery4', 'gallery5', 'gallery6', 'gallery7', 'gallery8']
     }
     return render(request, 'view/index.html', context)

def django_about(request):
    context = {
        "uId": getSession(request),
    }
    return render(request, 'view/about-us.html', context)

def django_activities(request):
     context = {
         "uId": getSession(request),
         "daysOfWeek": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
     }
     return render(request, 'view/activities.html', context)

def django_gallery(request):
     context = {
         "uId": getSession(request),
         "img": ['gallery1', 'gallery2', 'gallery3', 'gallery4', 'gallery5', 'gallery6', 'gallery7', 'gallery8']
     }
     return render(request, 'view/gallery.html', context)

def django_contact(request):
     context = {
        "uId": getSession(request),
     }
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
     return render(request, 'view/contact.html', context)

def django_request(request):
     context = {
        "uId": getSession(request),
     }
     return render(request, 'view/request.html', context)

def getSession(request):
    uId = ''
    if request.method == 'POST':
        if request.session.has_key('user_id'):
            request.session.flush()
            uId = "Null"
            print("Session", uId)
        return uId
    if 'user_id' in request.session:
        uId = request.session['user_id']
        print("Session", uId)
        return uId
    else:
        uId = "Null"
        print("Session", uId)
        return uId