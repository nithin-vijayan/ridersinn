# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Profile,Post,Usermessage,Friendship,FriendshipRequest

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Usermessage)
admin.site.register(Friendship)
admin.site.register(FriendshipRequest)
