# kitchen/views.py
# Programmers: Jeff C Cheng, Allen Sun, Kevin Wei, and Kevin Ortiz
# Last Modified: 11/1/2020
# pass titles and request through context

from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Recipe
from django.db.models import Q

def home(request):
  context = {
    'title': 'Home'
  }
  return render(request, 'kitchen/home.html', context)

def search(request):
  # set defaults
  title = "NONE"
  author = "NONE"
  content = "NONE"

  if request.method == 'POST':
    if request.POST['title']:
      title = request.POST['title']

    if request.POST['author']:
      author = request.POST['author']

    if request.POST['content']:
      content = request.POST['content']



  recipes = Recipe.objects.filter(Q(title__icontains=title)|Q(author__username=author)|Q(content__icontains=content))

  context = {
    'title': 'Search',
    'recipes': recipes
  }
  return render(request, 'kitchen/search.html', context)

def about(request):
  context = {
    'title': 'About'
  }
  return render(request, 'kitchen/about.html', context)

def allen_sun(request):
  context = {
    'title': 'Allen Sun'
  }
  return render(request, 'kitchen/allen_sun.html', context)

def jeff_cheng(request):
  context = {
    'title': 'Jeff C Cheng'
  }
  return render(request, 'kitchen/jeff_cheng.html', context)

def kevin_ortiz(request):
  context = {
    'title': 'Kevin Ortiz'
  }
  return render(request, 'kitchen/kevin_ortiz.html', context)

def groups(request):
  context = {
    'title': 'Groups'
  }
  return render(request, 'kitchen/groups.html', context)

def profile(request):
  context = {
    'title': 'Profile'
  }
  return render(request, 'kitchen/profile.html', context)

def log_in(request):
  context = {
    'title': 'Log In'
  }
  return render(request, 'kitchen/log_in.html', context)

def sign_up(request):
  context = {
    'title': 'Sign Up'
  }
  return render(request, 'kitchen/sign_up.html', context)