# kitchen/admin.py
# Programmer: Jeff C Cheng
# Last Modified: 11/6/2020
# register recipe model here

from django.contrib import admin
from .models import Recipe

admin.site.register(Recipe)