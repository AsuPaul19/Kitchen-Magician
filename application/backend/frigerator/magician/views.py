from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    content = {
        "title": "Frigerator Magician", 
    }
    return render(request, 'home.html', content)