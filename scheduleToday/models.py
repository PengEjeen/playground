from django.db import models
from django.utils import timezone
# Create your models here.

class Schedule(models.Model):
    schedule_id = models.CharField(max_length=5)    #filled with hash function
    title = models.CharField(max_length=20)
    description = models.TextField()
    dateTimeOfUpload = models.DateTimeField(auto_now=True)
