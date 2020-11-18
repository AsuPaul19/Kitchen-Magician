from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render
from django.shortcuts import redirect
# from django.contrib import messages
# from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Profile


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
        elif User.objects.filter(email=email).exists(): #unique email
            context['error'] = f'The email {email} already used.'
        elif password1 != password2:
            context['error'] = 'The two password fields didn’t match.'
        else:
            # create a user
            user = User.objects.create_user(username=username, password=password1, email=email)
            user.save()
            # create the profile
            user_profile = Profile(user=user)
            user_profile.save()
            return redirect('login')

    return render(request, "signup.html", context)


def login(request):
    # redirect to home page if user is already logged in
    if request.user.is_authenticated:
        return redirect('home')

    context = {
        'title': 'Login',
    }
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user authentication check
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            # if 'next' in request.GET:
            next_page = request.GET.get('next', False)
            # redirect to precious page once log in
            if next_page: 
                return HttpResponseRedirect(next_page)
            # redirect to home page if now page requested 
            else:
                return redirect('home')
        else:
            context['account'] = 'Hmmm, not a valid user name or password' # send message if it is wrong
            return render(request, 'login.html', context)

    return render(request, 'login.html', context)


def login_signup(request):

    return render(request, 'login_signup.html')

def forgot_password(request):
    context = {
        'title': 'Forgot Password'
    }
    return render(request, 'forgot_password.html', context)

@login_required
def user_profile(request, username=None):
    # handle user names and unmatched links
    if request.user.is_authenticated:
        context = {
            'title': 'Profile'
        }
        return render(request, 'user_profile.html', context)

    else:
        return login(request)

# below is for the images
recipes_section = {
    "1001": {
        "id": "1001",
        "img": "about/images/team/1NP.jpg",
        "name": "Recipe",
        "title": "Recipe 1",

    },
    "1002": {
        "id": "1002",
        "img": "about/images/team/2JC.jpg",
        "name": "Recipe",
        "title": "Recipe 2",

    },
    "1003": {
        "id": "1003",
        "img": "about/images/team/3AS.jpg",
        "name": "Recipe",
        "title": "Recipe 3",
    },
    "1004": {
        "id": "1004",
        "img": "about/images/team/4PA.jpg",
         "name": "Recipe",
        "title": "Recipe 4",
    },
    "1005": {
        "id": "1005",
        "img": "about/images/team/5KO.jpg",
        "name": "Recipe",
        "title": "Recipe 5",
    },

    "1006": {
        "id": "1006",
        "img": "about/images/team/6KW.jpg",
        "name": "Recipe",
        "title": "Recipe 6",
    },

    "1007": {
        "id": "1007",
        "img": "about/images/team/6KW.jpg",
        "name": "Recipe",
        "title": "Recipe 7",
    },

    "1008": {
        "id": "1008",
        "img": "about/images/team/6KW.jpg",
        "name": "Recipe",
        "title": "Recipe 8",
    },

    "1009": {
        "id": "1006",
        "img": "about/images/team/6KW.jpg",
        "name": "Recipe",
        "title": "Recipe 9",
    },

    "1010": {
        "id": "1006",
        "img": "about/images/team/6KW.jpg",
        "name": "Recipe",
        "title": "Recipe 10",
    }
}

favorites_section = {
    "1001": {
        "id": "1001",
        "img": "about/images/team/1NP.jpg",
        "name": "Favorite",
        "title": "Favorite 1",

    },
    "1002": {
        "id": "1002",
        "img": "about/images/team/2JC.jpg",
        "name": "Favorite",
        "title": "Favorite 2",

    },
    "1003": {
        "id": "1003",
        "img": "about/images/team/3AS.jpg",
        "name": "Favorite",
        "title": "Favorite 3",
    },
    "1004": {
        "id": "1004",
        "img": "about/images/team/4PA.jpg",
         "name": "Favorite",
        "title": "Favorite 4",
    },
    "1005": {
        "id": "1005",
        "img": "about/images/team/5KO.jpg",
        "name": "Favorite",
        "title": "Favorite 5",
    },

    "1006": {
        "id": "1006",
        "img": "about/images/team/6KW.jpg",
        "name": "Favorite",
        "title": "Favorite 6",
    },

    "1007": {
        "id": "1007",
        "img": "about/images/team/6KW.jpg",
        "name": "Recipe",
        "title": "Recipe 7",
    },

    "1008": {
        "id": "1008",
        "img": "about/images/team/6KW.jpg",
        "name": "Favorite",
        "title": "Favorite 8",
    },

    "1009": {
        "id": "1009",
        "img": "about/images/team/6KW.jpg",
        "name": "Favorite",
        "title": "Favorite 9",
    },

    "1010": {
        "id": "1010",
        "img": "about/images/team/6KW.jpg",
        "name": "Favorite",
        "title": "Favorite 10",
    }
}
# @login_required
# def account(request):
#     return profile(request)