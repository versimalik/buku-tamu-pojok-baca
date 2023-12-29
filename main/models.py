from django.db import models

# Create your models here.

class Guest(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    DateTime = models.DateTimeField()

    
