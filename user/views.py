from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import *
from datetime import date

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

# def django_login(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             try:
#                 uName = request.POST['email']
#                 uPwd = request.POST['pwd']
#                 user = authenticate(email=uName, pwd=uPwd)
#
#                 if user is not None:
#                     login(request, user)
#                     # messages.success(request, 'You are Login Successfully...')
#                     return redirect('index')
#                 else:
#                     return redirect('login')
#             # uDetail = User.objects.get(email=uName, pwd=uPwd)
#                 # if uDetail:
#                 #     request.session['user_id'] = uDetail.id
#                 #     return redirect('index')
#             except ObjectDoesNotExist:
#                 return render(request, 'view/login.html', {"txtErr": "Please enter Valid EmailId Or Password"})
#         else:
#             return render(request, 'view/login.html')
#     else:
#         return HttpResponseRedirect('/index/')


# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect('/dashboard/login')


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
     req = Requests.objects.filter(status="Accepted")
     print("Request is ", req)
     context = {
         "uId": getSession(request),
         "req": req,
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
         if request.POST.get('email'):
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
     uid = getSession(request)
     curr_user = User.objects.filter(id=uid)
     print("Current User is ", curr_user)
     context = {
        "uId": getSession(request),
        "curr_user": curr_user,
     }
     curDate = date.today()
     dt = curDate.strftime("%Y-%m-%d")
     if request.method == 'POST':
         if request.POST.get('whatFor'):
             name = request.POST['fName']
             whatFor = request.POST['whatFor']
             quantity = request.POST['quantity']
             try:
                adharcard = request.FILES['adharcard']
             except KeyError:
                 adharcard = 'images/adharcard/adharcard.jpg'
             try:
                 prescription = request.FILES['prescription']
             except KeyError:
                 prescription = 'images/adharcard/adharcard.jpg'
             objRequests = Requests()
             objRequests.user_id = context["uId"]
             objRequests.name = name
             objRequests.whatFor = whatFor
             objRequests.quantity = quantity
             objRequests.date = dt
             objRequests.adharcard = adharcard
             objRequests.prescription = prescription
             objRequests.save()
             return redirect('activities')
     return render(request, 'view/request.html', context)

def getSession(request):
    uId = ''
    if request.method == 'POST':
        if request.POST.get('logout'):
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