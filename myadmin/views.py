from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from user.models import User, Requests

# Create your views here.
def django_admin_panel(request):
     if request.method == "POST":
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
     datauser = User.objects.all()
     datarequest = Requests.objects.all()
     totaluser = datauser.count()
     totalrequest = datarequest.count()
     totaldonation = 0
     totalpending = 0
     totalapproval = 0
     totalreject = 0
     for x in datarequest:
          if x.status == "Sucessfull":
               totaldonation += 1
          elif x.status == "pending":
               totalpending += 1
          elif x.status == "Accepted":
               totalapproval += 1
          else:
               totalreject += 1
     try:
          aId = request.session['admin_id']
     except KeyError:
          return redirect('alogin')
     aDetail = MyAdmin.objects.get(id=aId)
     context = {
          "aId": aDetail.aName,
          "totaluser": totaluser,
          "totalrequest": totalrequest,
          "totaldonation": totaldonation,
          "totalpending": totalpending,
          "totalapproval": totalapproval,
          "totalreject": totalreject,
     }
     if request.method == 'GET':
          logout = request.GET.get('logout')
          if logout:
               if request.session.has_key('admin_id'):
                    request.session.flush()
               return redirect('alogin')
     # if request.method == 'POST':
     #      if request.POST.get('logout'):
     #           if request.session.has_key('admin_id'):
     #                request.session.flush()
     #           return redirect('alogin')
     return render(request,'Myadmin_panel/admin.html',context)


def django_admin_alluser(request):
     aId = request.session['admin_id']
     aDetail = MyAdmin.objects.get(id=aId)
     data = User.objects.all()
     context = {
          "aId": aDetail.aName,
          "alldata": data
     }
     return render(request,'Myadmin_panel/alluser.html',context)

def django_admin_changepassword(request):
     aId = request.session['admin_id']
     aDetail = MyAdmin.objects.get(id=aId)
     context = {
          "aId": aDetail.aName,
     }
     return render(request, 'Myadmin_panel/changepassword.html',context)

def django_admin_request(request):
     aId = request.session['admin_id']
     aDetail = MyAdmin.objects.get(id=aId)
     Request = Requests.objects.all()
     context = {
          "aId": aDetail.aName,
          "Request": Request,
     }
     return render(request, 'Myadmin_panel/request.html', context)

def request_check(request):
     if request.method == "POST":
          objRequest = Requests()
          objRequest.id = request.POST['id']
          objRequest.status = request.POST['request']
          objRequest.save(update_fields=['status'])
          return HttpResponseRedirect('/myadmin/Request')
