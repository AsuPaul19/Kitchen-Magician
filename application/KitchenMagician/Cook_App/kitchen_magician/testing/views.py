from django.shortcuts import render

# Create your views here.
def testing(request):
    context = {
        'title': 'Testing'

    }

    return render(request, 'testing/testing.html', context)