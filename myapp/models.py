from django.db import models

# Create your models here.
class usermessage(models.Model):
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=100,default='null')
    message=models.CharField(max_length=1000)