# users/forms.py
# Programmer: Jeff C Cheng
# Last Modified: 11/6/2020
# added app urls for kitchen
# added app url for user registration


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# create a new form for custom fields
class UserRegisterForm(UserCreationForm):
  # default is required = True
  email = forms.EmailField()

  class Meta:
    # the model that will be affected
    model = User
    
    # display these fields only
    fields = ['username', 'email', 'password1', 'password2']
