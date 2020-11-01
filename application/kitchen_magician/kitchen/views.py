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
  content = "NONE"
  author = "NONE"
  title = "NONE"

  if request.method == 'POST':
    if request.POST['content']:
      content = request.POST['content']

    if request.POST['author']:
      author = request.POST['author']

    if request.POST['title']:
      title = request.POST['title']

  recipes = Recipe.objects.filter(Q(author__username=author)|Q(content__icontains=content)|Q(title__icontains=title))

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