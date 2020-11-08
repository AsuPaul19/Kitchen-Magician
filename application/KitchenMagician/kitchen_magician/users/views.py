from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User



def signup(request):
    context = {
        'title': 'Login',
        'error' : '',
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username).exists(): # user already exists
            context['error'] = f'The user {username} already exists.'
        elif password1 != password2:
            context['error'] = 'The two password fields didn’t match.'
        # TODO - Check Email address
        else:
            # create a user
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            return redirect('login')




    # if request.method == 'POST':
    #     form = UserRegisterForm(request.POST)
    #     print(request.POST)
    #     print("==========")
    #     print(form)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'{username}, welcome to join us!')
    #         return redirect('login')
    # else:
    #     context['account'] = 'Hmmm, not a valid user name or password' # send message is it is wrong


    return render(request, "signup.html", context)


def login(request):
    context = {
        'title': 'Login',
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'{username} : {password}')
        # user authentication check
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            context['account'] = 'Hmmm, not a valid user name or password' # send message is it is wrong
            return render(request, 'login.html', context)

    return render(request, 'login.html', context)


def login_signup(request):

    return render(request, 'login_signup.html')

@login_required
def profile(request):
    # handle user names and unmatched links
    if request.user.is_authenticated:
        context = {
            'title': 'Profile'
        }
        return render(request, 'profile.html', context)

    else:
        return login(request)

@login_required
def account(request):
    return profile(request)