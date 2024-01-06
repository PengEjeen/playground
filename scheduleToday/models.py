from django.db import models
from django.utils import timezone
# Create your models here.

class Schedule(models.Model):
    schedule_id = models.CharField(max_length=5)    #filled with hash function
    title = models.CharField(max_length=20)
    description = models.TextField()
    cell_ids = models.JSONField(blank=True,
            null=True
            )
    dateTimeOfUpload = models.DateTimeField(auto_now=True)

class Cell(models.Model):   
    cell_id = models.CharField(max_length=7)
    cell_mode = models.CharField(max_length=20)
    place_id = models.JSONField(null=True,
            blank=True
            )


