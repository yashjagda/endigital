from django.db import models
from django.db.models.signals import pre_save


# Create your models here.
class UserDetails(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(blank=True, max_length=200)
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField(blank=True)
    contacted = models.BooleanField(default=False)
    status = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.name} - {self.phone} - {self.contacted} - {self.status}'


class HomePageContent(models.Model):
    banner_image1 = models.TextField(blank=True)
    banner1_h1 = models.TextField(blank=True)
    banner1_caption = models.TextField(blank=True)
    banner_image2 = models.TextField(blank=True)
    banner2_h1 = models.TextField(blank=True)
    banner2_caption = models.TextField(blank=True)
    banner_image3 = models.TextField(blank=True)
    banner3_h1 = models.TextField(blank=True)
    banner3_caption = models.TextField(blank=True)

    section1_heading = models.CharField(max_length=100, blank=True)
    section1_content = models.TextField(blank=True)

    section2_heading = models.CharField(max_length=200, blank=True)
    section2_content = models.TextField(blank=True)
    section2_imageURL = models.TextField(blank=True)

    section3_content = models.TextField(blank=True)
    section3_percentage1 = models.CharField(max_length=100, blank=True)
    section3_percentage1_heading = models.CharField(max_length=200, blank=True)
    section3_percentage2 = models.CharField(max_length=100, blank=True)
    section3_percentage2_heading = models.CharField(max_length=200, blank=True)
    section3_percentage3 = models.CharField(max_length=100, blank=True)
    section3_percentage3_heading = models.CharField(max_length=200, blank=True)

    section4_heading = models.CharField(max_length=100, blank=True)
    section4_content = models.TextField(blank=True)

    section5_imageURL = models.TextField(blank=True)

    def __str__(self):
        return "HomePage"


class Blogs(models.Model):
    imageURL = models.TextField(blank=True)
    title = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=20, blank=True)
    author = models.CharField(max_length=40, blank=True)
    dateDay = models.CharField(max_length=2, blank=True)
    dateMonth = models.CharField(max_length=3, blank=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title


class ServicesOfferedContent1(models.Model):
    imageURL = models.TextField(blank=True)
    services_Name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.services_Name


class ServicesOfferedContent2(models.Model):
    imageURL = models.TextField(blank=True)
    services_Name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.services_Name


class ServicesDetail(models.Model):
    imageURL = models.TextField(blank=True)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
