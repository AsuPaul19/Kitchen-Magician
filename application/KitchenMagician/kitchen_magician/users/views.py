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
from django.contrib.auth.models import User
<<<<<<< HEAD
=======


>>>>>>> dev_backend
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
        'title': 'Profile'
    }
    return render(request, 'forgot_password.html', context)
@login_required
def user_profile(request, username=None):
    # handle user names and unmatched links
    if request.user.is_authenticated:
        context = {
            'title': 'Profile'
        }
        # print(request.user)
        # user = User.objects.filter(username=request.user).first()
        user_recipes = profile_recipes(request.user.recipe_set.all())
        context['user_recipes'] = user_recipes
        user_favorite = profile_recipes([favorite.recipe for favorite in request.user.recipefavorite_set.all()])
        context['user_favorites'] = user_favorite
        return render(request, 'user_profile.html', context)
    else:
        return login(request)
def profile_recipes(recipes=None):
    recipes_data = []
    for recipe in recipes:
        recipe_name= recipe.name
        recipe_id = recipe.id
        recipe_image = recipe.recipeimage_set.all()[0].image
        recipes_data.append(
            {
                'recipe_name': recipe_name,
                'recipe_id': recipe_id,
                'recipe_image': recipe_image,
            }
        )
    return recipes_data
# @login_required
# def account(request):
#     return profile(request)
