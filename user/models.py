
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

   # def image_tag1(self):
   #    if self.adharcard:
   #       return mark_safe('<img src="%s" style="width:120px;height:120px" />' % self.adharcard.url)
   #    else:
   #       return 'no image found'
   #
   # def image_tag2(self):
   #    if self.prescription:
   #       return mark_safe('<img src="%s" style="width:120px;height:120px" />' % self.prescription.url)
   #    else:
   #       return 'no image found'

class Contact(models.Model):
   name = models.CharField(max_length=20, null=True)
   email = models.CharField(max_length=40, null=True)
   subject = models.CharField(max_length=20, null=True)
   message = models.CharField(max_length=50, null=True)