

from django.urls import path
from . import views

# kitchen_magician project routes default to kitchen app routes
urlpatterns = [
    path('', views.home, name='kitchen_home'),
    path('about/', views.about, name='kitchen_about'),
    path('groups/', views.groups, name='kitchen_groups'),
    path('profile/', views.profile, name='kitchen_profile'),
    path('log_in/', views.log_in, name='kitchen_log_in'),
    path('sign_up/', views.sign_up, name='kitchen_sign_up'),
]
