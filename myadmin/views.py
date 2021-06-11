from django.shortcuts import render

# Create your views here.
def django_admin(request):
     return render(request,'admin/admin.html')