from django.db import models

# Create your models here.
class Contact(models.Model):
   name = models.CharField(max_length=20, default='', null=False)
   email = models.CharField(max_length=40, default='', null=False)
   subject = models.CharField(max_length=20, default='', null=False)
   message = models.CharField(max_length=50, default='', null=False)