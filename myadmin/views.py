from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render ,redirect
from .models import *


# Create your views here.
def django_admin_panel(request):
     if request.method=="POST":
          try:
            aName = request.POST['email']
            aPwd = request.POST['pwd']
            aDetail = MyAdmin.objects.get(email=aName, pwd=aPwd)
            if aDetail:
                request.session['admin_id'] = aDetail.id
                return redirect('admindashboard')
          except ObjectDoesNotExist:
            return render(request, 'Myadmin_panel/login.html', {"txtErr": "Please Enter Valid Email Id Or Password"})
     else:
          return render(request, 'Myadmin_panel/login.html')

def django_admin_dashboard(request):

     return render(request,'Myadmin_panel/admin.html')