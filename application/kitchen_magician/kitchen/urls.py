# kitchen/urls.py
# Programmer: Jeff C Cheng
# Last Modified: 11/1/2020
# define all app-specific routes here

from django.urls import path
from . import views

# kitchen_magician project routes default to kitchen app routes
urlpatterns = [
    path('', views.home, name='kitchen_home'),
    path('home/', views.home, name='kitchen_home'),
    path('search/', views.search, name='kitchen_search'),
    path('about/', views.about, name='kitchen_about'),
    path('allen_sun/', views.allen_sun, name='kitchen_allen_sun'),
    path('jeff_cheng/', views.jeff_cheng, name='kitchen_jeff_cheng'),
    path('kevin_ortiz/', views.kevin_ortiz, name="kitchen_kevin_ortiz"),
    path('kevin_wei/', views.kevin_wei, name="kitchen_kevin_wei"),
    path('nicole_pang/', views.nicole_pang, name="kitchen_nicole_pang"),
    path('paul_asu/', views.paul_asu, name="kitchen_paul_asu"),    
    path('groups/', views.groups, name='kitchen_groups'),
    path('profile/', views.profile, name='kitchen_profile'),
    path('log_in/', views.log_in, name='kitchen_log_in'),
]