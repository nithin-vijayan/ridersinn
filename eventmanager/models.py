from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    eventtitle = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    eventstart = models.DateField(null=True, blank=True)
    eventend = models.DateField(null=True, blank=True)
    members = models.IntegerField(null=True, blank=True, default=0)
