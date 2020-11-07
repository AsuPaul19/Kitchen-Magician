# users/views.py
# Programmer: Jeff C Cheng
# Last Modified: 11/6/2020
# use Django built-in form for registration page


from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
  # create the form
  form = UserCreationForm()

  context = {
    {'form': form}
  }
  return render(request, 'users/register.html', context)
