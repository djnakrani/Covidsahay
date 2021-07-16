import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import *
from myadmin.models import *
from datetime import date
from django.contrib import messages

# Create your views here.
def django_login(request):
    if request.method == 'POST':
        try:
            uName = request.POST['email']
            uPwd = request.POST['pwd']
            uDetail = User.objects.get(email=uName, pwd=uPwd)
            if uDetail:
                request.session['user_id'] = uDetail.id
                messages.success(request, "You Have successfully Login")
                return HttpResponseRedirect('/')
        except ObjectDoesNotExist:
            messages.warning(request, "Please enter Valid EmailId Or Password")
            return render(request, 'view/login.html')
    else:
        return render(request, 'view/login.html')

def django_register(request):
     if request.method == 'POST':
         if request.POST.get('register'):
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
             pwd = request.POST['pwd']
             conPwd = request.POST['conPwd']
             if pwd == conPwd:
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
                 objUser.pwd = pwd
                 objUser.save()
                 messages.success(request, "You have successfully Registered")
                 return HttpResponseRedirect('login')
             else:
                 messages.error(request, "Password Does not Match")
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
     }
    if request.method == "POST":
        if request.POST.get('allsearch'):
            whats = request.POST['allsearch'].split(",")
            # print(whats)
            if whats:
                # print("what")
                context = activities(request, whats)
            else:
                context = activities(request, "")
                # print("else")
        elif request.POST.get('req'):
            uid = getSession(request)
            curDate = date.today()
            dt = curDate.strftime("%Y-%m-%d")
            rId = request.POST['rId']
            print(rId, dt, uid)
            objReq = Requests()
            objReq.id = rId
            objReq.status = "DAccepted"
            objDonor = Donor()
            objDonor.requests_id = rId
            objDonor.user_id = context["uId"]
            objDonor.date = dt
            objDonor.save()
            objReq.save(update_fields=['status'])
            context = activities(request, "")
            messages.success(request, "You Donate successfully.")
            return HttpResponseRedirect('/activities', context)
        else:
            context = activities(request, "")
        return render(request, 'view/activities.html', context)
    else:
        context = activities(request, "")
        return render(request, 'view/activities.html', context)

def activities(request, need):
    # print(need)
    if need:
        user = User.objects.filter(city__in=need) | User.objects.filter(state__in=need) | User.objects.filter(
            area__in=need)
        # print(user.exists())
        if not user.exists():
            req = Requests.objects.filter(status="Accepted").order_by('-date') & (Requests.objects.filter(whatFor__in=need))
        else:
            req = Requests.objects.filter(status="Accepted").order_by('-date') & (Requests.objects.filter(whatFor__in=need).filter(user__in=user))
    else:
        req = Requests.objects.filter(status="Accepted").order_by('-date')

    opwhat = Requests.objects.values_list('whatFor', flat=True).distinct()
    city = User.objects.values_list('city', flat=True).distinct()
    state = User.objects.values_list('state', flat=True).distinct()
    area = User.objects.values_list('area', flat=True).distinct()
    context = {
        "uId": getSession(request),
        "req": req,
        "opwhat": opwhat,
        "city": city,
        "state": state,
        "area": area,
    }
    return context

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
         if request.POST.get('contact'):
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
             messages.success(request, "Your Message are successfully Sent.")
     return render(request, 'view/contact.html', context)

def django_request(request):
     uid = getSession(request)
     if uid == "null":
         curr_user = User.objects.filter(id=uid)
         print("Current User is ", curr_user)
         context = {
            "uId": getSession(request),
            "curr_user": curr_user,
         }
         curDate = date.today()
         dt = curDate.strftime("%Y-%m-%d")
         if request.method == 'POST':
             if request.POST.get('req'):
                 name = request.POST['fName']
                 whatFor = request.POST['whatFor']
                 if whatFor == "Others":
                     whatFor = request.POST['whatOthers']
                 quantity = request.POST['quantity']
                 try:
                    adharcard = request.FILES['adharcard']
                 except KeyError:
                     adharcard = 'images/adharcard/adharcard.jpg'
                 try:
                     prescription = request.FILES['prescription']
                 except KeyError:
                     prescription = 'images/prescription/prec.png'
                 objRequests = Requests()
                 objRequests.user_id = context["uId"]
                 objRequests.name = name
                 objRequests.whatFor = whatFor
                 objRequests.quantity = quantity
                 objRequests.date = dt
                 objRequests.adharcard = adharcard
                 objRequests.prescription = prescription
                 objRequests.save()
                 messages.success(request, "Your Request are successfully Created")
                 return HttpResponseRedirect('/activities')
     else:
         return redirect('index')
     return render(request, 'view/request.html', context)


def django_myrequest(request):
     Request = Requests.objects.all()
     Donors = Donor.objects.all()
     print("Donors", Donors)
     print(type(Donors))
     context = {
         "uId": getSession(request),
         "Request": Request,
         "Donors": Donors,
     }
     if request.method == 'POST':
         if request.POST.get('request'):
             rid = request.POST['rId']
             print(rid)
             Request.filter(id=rid).delete()
     return render(request, 'view/myrequest.html', context)

def django_mydetails(request):
     uId = getSession(request)
     if request.method == 'POST': 
         if request.POST.get('detailschange'):
            objUser = User()
            objUser.id = request.POST['id']
            objUser.fName = request.POST['fName']
            objUser.lName = request.POST['lName']
            objUser.mono = request.POST['mono']
            objUser.gender = request.POST['gender']
            objUser.dob = request.POST['dob']
            objUser.bGrp = request.POST['bGrp']
            objUser.email = request.POST['email']
            objUser.state = request.POST['state']
            objUser.city = request.POST['city']
            objUser.area = request.POST['area']
            objUser.add = request.POST['add']
            objUser.pwd = request.POST['pwd']
            #  print(id,fName,lName,mono,gender,dob,bGrp,email,state,city,area,add,pwd)
            objUser.save()
            messages.success(request, "Your Data successfully Upgrated.")
     if uId == "Null":
         return redirect('index')
     else:
        user = User.objects.filter(id=uId)
        #  print(user)
        context = {
            "uId": uId,
            "user": user,
        }
        return render(request, 'view/mydetails.html', context)

def django_changeuserpassword(request):
    uId=getSession(request)
    if request.method == "POST":
        if request.POST.get('changepassword'):
            objUser = User()
            objUser.id = uId
            objUser.pwd = request.POST['cnew']
            objUser.save(update_fields=['pwd'])
            messages.success(request, "Your Password Successfully Upgrated.")

    if uId == "Null":
         return redirect('index')
    else:
        user = User.objects.filter(id=uId)
        context = {
            "uId": uId,
            "user": user,
        }
        return render(request, 'view/changepassword.html', context)

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

