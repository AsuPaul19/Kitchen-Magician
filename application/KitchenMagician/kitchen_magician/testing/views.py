from django.shortcuts import render

# Create your views here.
def testing(request):
    context = {
        'title': 'Testing',
        'diets': 'Gluten Free'
    }

    return render(request, 'testing/testing.html', context)