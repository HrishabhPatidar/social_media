# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ImageUpload

class UploadAdmin(admin.ModelAdmin):
    list_display = ('user','caption','user_like')

admin.site.register(ImageUpload, UploadAdmin)
