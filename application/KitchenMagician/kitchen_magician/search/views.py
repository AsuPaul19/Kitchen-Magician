from typing import Counter
from django.shortcuts import render
from recipe.models import Recipe
from recipe.models import RecipeInformation
from django.contrib.auth.models import User
from recipe.models import RecipeTest
from django.db.models import Q


def search(request):
    select = "NONE"
    keyword = "NONE"
    recipes = None
    if request.method == 'POST':
        # This is the search when it's done through the navbar
        if 'filter' in request.POST:
            select = request.POST['filter']
            keyword = request.POST['keyword']
            if select == 'none':
                recipes = RecipeTest.objects.filter(Q(title__icontains=keyword) | Q(
                author__username=keyword) | Q(content__icontains=keyword))
            elif select == 'title':
                recipes = RecipeTest.objects.filter(Q(title__icontains=keyword))
            elif select == 'author':
                recipes = RecipeTest.objects.filter(Q(author__username=keyword))
            elif select == 'content':
                recipes = RecipeTest.objects.filter(Q(content__icontains=keyword))
        else:
            # This is the search when it's done through the search page
            title = "NONE"
            author = "NONE"
            content = "NONE"
            if request.POST['title']:
                title = request.POST['title']
            if request.POST['author']:
                author = request.POST['author']
            if request.POST['content']:
                content = request.POST['content']
            recipes = RecipeTest.objects.filter(Q(title__icontains=title) | Q(
            author__username=author) | Q(content__icontains=content))

    context = {
        'title': 'Search',
        'recipes': recipes
    }
    return render(request, 'search.html', context)

# Allen's
# def search(request):
#     context = {
#         'title': 'Search',
#     }

#     if request.method == 'POST':
#         keywords = request.POST['keywords']
#         context['keywords'] = keywords
#         print(context['keywords'])
#         context['recipes'] = search_information(keywords)
#         print(context['recipes'])
#         return render(request, 'search.html', context)
#     return render(request, 'search.html', context)


# def filter(keywords):
#     results = []
#     users = User.objects.filter(username=keywords)
#     for user in users:
#         recipes = Recipe.objects.filter(user=user)
#         for recipe in recipes:
#             results.append(f'{recipe.name} by {recipe.user}')
#     return results

# def search_information(keywords):
#     results = []
#     infos = RecipeInformation.objects.filter(information__contains=keywords)
#     for info in infos:
#         recipe = info.recipe_id
#         results.append(f'{recipe.name} by {recipe.user}')
#     return results
