from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:recipe_id>/', views.recipe_view, name='recipe'),
    path('create-recipe/', views.create_recipe, name='create_recipe'),
    path('submit-recipe/', views.submit_recipe, name='submit_recipe'),
    path('upload-test/', views.upload_test, name='upload_file'),
    path('404/', views.not_found, name='not_found'),

]    

