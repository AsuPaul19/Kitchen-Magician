from django.shortcuts import render

# Create your views here.
def recipe(request):
    context = {
        'title': 'RECIPE'
    }
    return render(request, 'recipe.html', context)