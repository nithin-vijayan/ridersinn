# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db import models
import userprofile
import datetime

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(default='anonymous_user.jpg')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('userprofile:profile', args=[str(self.user.username)])

class Post(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    postcontent = models.TextField(max_length=500, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

class Usermessage(models.Model):
    fromuser= models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    touser= models.ForeignKey(User,on_delete=models.CASCADE,related_name="recipient")
    content = models.TextField(max_length=500, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

class FriendshipRequest(models.Model):
    from_user = models.ForeignKey(User, related_name="invitations_from")
    to_user = models.ForeignKey(User, related_name="invitations_to")
    message = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(default=datetime.datetime.now,
                                   editable=False)
    accepted = models.BooleanField(default=False)

class Friendship(models.Model):
    user = models.OneToOneField(User, related_name='friendship')
    friends = models.ManyToManyField('self', symmetrical=True)
