# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.http.response import HttpResponse
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,update_session_auth_hash,logout
from accountforms import UserForm,passwordResetForm
from tokens import account_activation_token
from django.contrib.auth.models import User
from userprofile import urls as userurl


def userSignup(request):
    if request.user:
        logout(request)
    if request.method=='POST':
        form =UserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = UserForm()
    return render(request,'signup.html',{'form':form})

def account_activation_sent(request):
    return HttpResponse("Email Send")

@login_required
def changePassword(request):
    form = passwordResetForm(user=request.user)
    if request.method=='POST':
        form =passwordResetForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('userprofile:profile')
    return render(request,'changepassword.html',{'form':form})

def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('userprofile:edit')
    else:
        return HttpResponse("Invalid URL")
