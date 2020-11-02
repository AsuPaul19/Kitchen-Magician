from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('<str:name>-<str:id>/', views.profile, name='about-profile'),
]
