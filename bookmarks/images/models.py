# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,blank=True)
    image = models.ImageField(upload_to='images/%Y/%M/%D')
    url = models.URLField()
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True,db_index=True)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='images_liked',blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Image, self).save(*args, **kwargs)



