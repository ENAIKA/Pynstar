# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Image, UserProfile, Comments

# Register your models here.
admin.site.register(Image)
admin.site.register(UserProfile)
admin.site.register(Comments)

