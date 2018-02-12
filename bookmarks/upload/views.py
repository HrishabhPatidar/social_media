# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm
from .models import ImageUpload





@login_required
def uploadation(request):
    usernamed = ImageUpload(user = request.user)
    if request.method == 'POST':
        imageform = ImageUploadForm(request.POST, request.FILES, instance= usernamed)
        if imageform.is_valid():
            new_image = imageform.save(commit=False)
            new_image.username = request.user
            new_image.save()
        return HttpResponseRedirect('/upload/imageupload/')

    else:
        imageform = ImageUploadForm()
    images = ImageUpload.objects.all()
    return render(request, 'upload/uploadimage.html/', {'imageform':imageform,'images':images})



def image_detail(request, id, slug):
    image = get_object_or_404(ImageUpload, id=id, slug=slug)
    return render(request,'upload/detail.html',{'section': 'upload','image': image})


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = ImageUpload.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
                return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})