from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.test, name='about'),
    path('test/', views.test, name='test'),
]
