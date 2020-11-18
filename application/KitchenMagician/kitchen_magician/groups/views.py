from django.shortcuts import render

# Create your views here.
def groups(request):
    context = {
        'title': 'GROUPS'
    }
    return render(request, 'groups/groups.html', context)

def group_forum(request):
    context = {
        'title': 'GROUPS_FORUM'
    }
    return render(request, 'groups/group_forum.html', context)