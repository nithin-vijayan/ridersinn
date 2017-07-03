# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Profile,Post,Usermessage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from userforms import ProfileForm,PostForm,MessageForm,FriendForm
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string

@login_required
def editprofile(request):
    instance=get_object_or_404(Profile,user=request.user)
    pform=ProfileForm(request.POST or None,request.FILES or None, instance=instance)
    if pform.is_valid():
        instance=pform.save(commit=False)
        instance.save()
        return redirect('userprofile/editprofile.html')
    return render(request, 'userprofile/editprofile.html', {'form': pform})

def friendrequest(request):
    data=dict()
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True
            touser = form.cleaned_data['touser']
            fromuser = request.user
        else:
            data['form_is_valid'] = False
    return JsonResponse(data)


def message(request):
    data=dict()

    if request.method == 'POST':
        print request.POST
        form = MessageForm(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True
            messageobject=form.save(commit=False)
            messageobject.touser=get_object_or_404(User, username=request.POST['touser'])
            messageobject.fromuser=request.user
            messageobject.save()
        else:
            data['form_is_valid'] = False
    else:
        pform = MessageForm()
        instance=get_object_or_404(User, username=request.GET['touser'])
        data['html_form'] = render_to_string('userprofile/message_partial.html',{'instance':instance,'postform':pform}, request=request)
    return JsonResponse(data)

def profile(request,username=None):
    usermessage=Usermessage.objects.filter(touser=request.user).order_by('-timestamp')[:3]
    if username and username!=request.user.username:
        instance=get_object_or_404(User, username= (username or request.user.username))
        posts=Post.objects.filter(user=instance).order_by('-timestamp')
        ishomepage=False
    else:
        instance=get_object_or_404(User, username= (username or request.user.username))
        posts=Post.objects.all().order_by('-timestamp')
        ishomepage=True
    return render(request, 'userprofile/profile.html', {'instance': instance, 'posts':posts, 'usermessage':usermessage,'ishomepage':ishomepage})

@login_required
def posts(request):
    print request.POST
    user=User.objects.get(username=request.user.username)
    post=Post.objects.create(user=user,postcontent=request.POST['post'])
    post.save()
    return redirect(user.profile)
