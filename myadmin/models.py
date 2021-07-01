from django.db import models

# Create your models here.
class MyAdmin(models.Model):
   fName = models.CharField(max_length=30, null=True)
   aName = models.CharField(max_length=20, null=True)
   aPwd = models.CharField(max_length=20, null=True)


