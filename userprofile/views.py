# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Profile,Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from userforms import ProfileForm
from django.contrib.auth.models import User

@login_required
def editprofile(request):
    instance=get_object_or_404(Profile,user=request.user)
    pform=ProfileForm(request.POST or None,request.FILES or None, instance=instance)
    if pform.is_valid():
        instance=pform.save(commit=False)
        instance.save()
        return redirect('userprofile/editprofile.html')
    return render(request, 'userprofile/editprofile.html', {'form': pform})


def profile(request,username=None):
    if username:
        instance=get_object_or_404(User, username= (username or request.user.username))
        posts=Post.objects.filter(user=instance).order_by('-timestamp')
    else:
        instance=get_object_or_404(User, username= (username or request.user.username))
        posts=Post.objects.all().order_by('-timestamp')
    return render(request, 'userprofile/profile.html', {'instance': instance, 'posts':posts})

@login_required
def posts(request):
    print request.POST
    user=User.objects.get(username=request.user.username)
    post=Post.objects.create(user=user,postcontent=request.POST['post'])
    post.save()
    return redirect(user.profile)
