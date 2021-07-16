from django.db import models

# Create your models here.
class MyAdmin(models.Model):
   aName = models.CharField(max_length=30, null=True)
   aEmail = models.CharField(max_length=30, null=True)
   aPwd = models.CharField(max_length=20, null=True)

class State(models.Model):
   name = models.CharField(max_length=30, null=True)

class City(models.Model):
   name = models.CharField(max_length=30, null=True)
   State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

