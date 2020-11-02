from django.shortcuts import render

# Create your views here.
def groups(request):
    context = {
        'title': 'GROUPS'
    }
    return render(request, 'groups.html', context)