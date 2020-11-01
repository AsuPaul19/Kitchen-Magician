# kitchen_magician/asgi.py
# Programmer: Jeff C Cheng
# Last Modified: 11/1/2020
# added app urls for kitchen

from django.contrib import admin
from django.urls import path, include

# kitchen_magician project routes default to kitchen app routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kitchen.urls')),
]
