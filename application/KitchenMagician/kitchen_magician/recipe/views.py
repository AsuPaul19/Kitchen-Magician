from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def recipe(request):
    context = {
        'title': 'RECIPE'
    }
    return render(request, 'recipe.html', context)

def create_recipe(request):
    context = {
        'title': 'CREATE RECIPES'
    }
    return render(request, 'create_recipe.html', context)


def submit_recipe(request):
    context = {
        'title': 'SUBMIT RECIPES'
    }
    if request.method == 'POST':
        data = request.POST
        print(data)
    return HttpResponse("Here's the text of submit recipe.")