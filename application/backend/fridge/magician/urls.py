from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/<str:name>-<str:id>', views.profile, name='profile'),
    path('test/', views.test, name='test'),
]
