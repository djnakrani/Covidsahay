
from django.db import models

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


class Contact(models.Model):
   name = models.CharField(max_length=20, null=True)
   email = models.CharField(max_length=40, null=True)
   subject = models.CharField(max_length=20, null=True)
   message = models.CharField(max_length=50, null=True)