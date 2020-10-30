from django.shortcuts import render
from .models import Recipe

def home(request):
  context = {
    'title': 'Home'
  }
  return render(request, 'kitchen/home.html', context)

def search(request):
  context = {
    'title': 'Search Results',
    'recipes': Recipe.objects.all()
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