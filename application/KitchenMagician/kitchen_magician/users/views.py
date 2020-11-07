from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserRegisterForm


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, welcome to join us!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'title': 'Login',
        'form': form,
    }
    return render(request, "signup.html", context)


def login(request):
    context = {
        'title': 'Login',
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'{username} : {password}')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            context['account'] = 'Hmmm, not a valid user name or password'
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