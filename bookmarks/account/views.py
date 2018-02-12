# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from upload.models import ImageUpload
from .models import Profile


from .forms import LogInForm, UserRegistrationForm, UserEditForm, ProfileEditForm

def base(request):
    return render(request, 'registration/base.html', {'this':'this is he'})

def user_login(request):
    if request.method == 'POST':
        loginform = LogInForm(request.POST)
        if loginform.is_valid():
            cd = loginform.cleaned_data
            user = authenticate(request,username= cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('login successfully')
                else:
                    return HttpResponse('desabled Account')
            else:
                return HttpResponseRedirect('/account/login/')

    else:
        loginform = LogInForm()
    return render(request, 'account/login.html/', {'loginform':loginform})

@login_required
def dashboard(request):
    images = ImageUpload.objects.all()
    return render(request, 'account/dashboard.html/', {'section':'dashboard','images':images })



def register(request):
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            new_user = registration_form.save(commit=False)
            new_user.set_password(registration_form.cleaned_data['password2'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/registration_done.html', {'registration_form':registration_form})
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'registration_form':registration_form})


@login_required
def edit(request):
    if request.method =='POST':
        user_edit_form = UserEditForm(instance=request.user, data=request.POST)
        profile_edit_form =ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save()
            profile_edit_form.save()
            return render(request, 'account/dashboard.html/', {'section':'dashboard'})
    else:
        user_edit_form = UserEditForm(instance=request.user)
        profile_edit_form = ProfileEditForm(instance=request.user.profile)

    return render(request,'account/edit.html',{'user_form': user_edit_form, 'profile_form': profile_edit_form})