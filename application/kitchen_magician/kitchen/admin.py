# kitchen/admin.py
# Programmer: Jeff C Cheng
# Last Modified: 11/1/2020
# register database model here

from django.contrib import admin
from django.contrib import admin
from .models import Recipe

admin.site.register(Recipe)