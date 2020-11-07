# user/views.py
# Programmer: Jeff C Cheng
# Last Modified: 11/6/2020
# now we save the user into the database

from django.shortcuts import render, redirect
# for flash messages
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):

  # POST request, fill the form with user data
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)

    # now validate the data
    if form.is_valid():      
      form.save()

      # get the user name
      username = form.cleaned_data.get('username')

      # inform the user that account has been successfully created
      messages.success(request, f'Account created for  {username}!')

      # success, let's redirect user back to home page
      return redirect('kitchen_home')
  
  else:
    # GET request, display blank form
    form = UserRegisterForm()
  context = {
    'form': form,
  }
  
  # if validation checks failed, render the form with error explanations
  return render(request, 'users/register.html', context)

  