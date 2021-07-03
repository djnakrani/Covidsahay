from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render ,redirect
from .models import *
from user.models import User,Requests


# Create your views here.
def django_admin_panel(request):
     if request.method=="POST":
          try:
            aName = request.POST['email']
            aPwd = request.POST['pwd']
            aDetail = MyAdmin.objects.get(aEmail=aName, aPwd=aPwd)
            if aDetail:
                request.session['admin_id'] = aDetail.id
                return redirect('admindashboard')
          except ObjectDoesNotExist:
            return render(request, 'Myadmin_panel/login.html', {"txtErr": "Please Enter Valid Email Id Or Password"})
     else:
          return render(request, 'Myadmin_panel/login.html')

def django_admin_dashboard(request):
     aId=request.session['admin_id']
     aDetail= MyAdmin.objects.get(id=aId)
     # print(aDetail.aName)
     context={
          "aId":aDetail.aName
     }
     return render(request,'Myadmin_panel/admin.html',context)


def django_admin_alluser(request):
     aId=request.session['admin_id']
     aDetail= MyAdmin.objects.get(id=aId)
     data = User.objects.all()
     context={
          "aId":aDetail.aName,
          "alldata":data
     }
     return render(request,'Myadmin_panel/alluser.html',context)

def django_admin_changepassword(request):
     aId=request.session['admin_id']
     aDetail= MyAdmin.objects.get(id=aId)
     # data = User.objects.all()
     context={
          "aId":aDetail.aName,
          # "alldata":data,
     }
     return render(request,'Myadmin_panel/changepassword.html',context)

def django_admin_request(request):
     aId=request.session['admin_id']
     aDetail= MyAdmin.objects.get(id=aId)
     Request = Requests.objects.all()
     context={
          "aId":aDetail.aName,
          "Request":Request,

     }
     return render(request,'Myadmin_panel/request.html',context)