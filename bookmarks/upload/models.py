# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.conf import settings

class ImageUpload(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
    image = models.ImageField(upload_to="upload_image")
    caption = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=False, blank=False)
    user_like = models.IntegerField(settings.AUTH_USER_MODEL,blank=True,default = 0)
    like = models.BooleanField(default=False)
    slug = models.CharField(max_length=40,default= username)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username + self.id)
            super(ImageUpload, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])




