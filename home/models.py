from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    number=models.IntegerField(default=0)

class Document(models.Model):
    title = models.CharField(max_length=20)
    uploadedFile = models.FileField(upload_to="result/")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)
