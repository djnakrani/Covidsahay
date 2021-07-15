import datetime

from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class User(models.Model):
   fName = models.CharField(max_length=20, null=True)
   lName = models.CharField(max_length=20, null=True)
   mono = models.BigIntegerField(null=True)
   gender = models.CharField(max_length=10, null=True)
   dob = models.CharField(max_length=10, null=True)
   bGrp = models.CharField(max_length=10, null=True)
   email = models.CharField(max_length=30, null=True)
   state = models.CharField(max_length=20, null=True)
   city = models.CharField(max_length=20, null=True)
   area = models.CharField(max_length=20, null=True)
   add = models.CharField(max_length=50, null=True)
   pwd = models.CharField(max_length=50, null=True)

class Requests(models.Model):
   name = models.CharField(max_length=20, null=True)
   user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   whatFor = models.CharField(max_length=40, null=True)
   quantity = models.CharField(max_length=20, default="1", null=True)
   date = models.CharField(max_length=20, null=True)
   adharcard = models.ImageField(upload_to='images/adharcard', null=True)
   prescription = models.ImageField(upload_to='images/prescription', null=True)
   status = models.CharField(max_length=20, default='pending', null=True)

class Donor(models.Model):
   user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   requests = models.ForeignKey(Requests, on_delete=models.SET_NULL, null=True)
   date = models.CharField(max_length=20, null=True)
   status = models.CharField(max_length=20, default='pending', null=True)

class Contact(models.Model):
   name = models.CharField(max_length=20, null=True)
   email = models.CharField(max_length=40, null=True)
   subject = models.CharField(max_length=20, null=True)
   message = models.CharField(max_length=50, null=True)