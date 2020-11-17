from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    # path('<str:name>-<str:id>/', views.profile, name='about-profile'),
    path('<str:keywords>/', views.search, name='search-keywords'),
]



