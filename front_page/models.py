from distutils.command.upload import upload
from django.db import models

# Create your models here.
## widget ##
# video 
 # upload video with a limited size
 # vission mission core values textfields with limited words
# noticeboard 
 # heading content 
# events calender

class CollegeInformation(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class VideoWidget(models.Model):
    video = models.FileField(upload_to='front_videos/')
    vision = models.TextField(max_length=500)
    mission = models.TextField(max_length=500)
    core_values = models.TextField(max_length=500)

    def __str__(self):
        return self.vision

from django.contrib.auth.models import User
from attendance.models import Department
class Noticeboard(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title