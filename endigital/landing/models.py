from django.db import models
from django.db.models.signals import pre_save


# Create your models here.
class UserDetails(models.Model): 
    name = models.CharField(max_length=200,blank=True)
    email = models.CharField(blank=True,max_length=200)
    phone = models.CharField(max_length=20,blank=True)
    subject = models.CharField(max_length=200,blank=True)
    message = models.TextField(blank=True)
    contacted = models.BooleanField(default=False)
    status = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return f'{self.name} - {self.phone} - {self.contacted} - {self.status}'


class Services(models.Model):
    service_content= models.TextField(blank=True)
    heading= models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.heading

class ServicesContent(models.Model):
    imageURL =  models.TextField(blank=True)
    serviceName = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.serviceName

class Blogs(models.Model):
    imageURL = models.TextField(blank=True)
    title = models.CharField(max_length=200,blank=True)
    category = models.CharField(max_length=20,blank=True)
    author = models.CharField(max_length=40,blank=True)
    dateDay = models.CharField(max_length=2,blank=True)
    dateMonth = models.CharField(max_length=3,blank=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    
    def __str__(self):
        return self.title














