from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title': 'LOGIN'
    }
    return render(request, 'login.html', context)

