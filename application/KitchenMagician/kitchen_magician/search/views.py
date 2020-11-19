from django.shortcuts import render
from .search_recipe import SearchRecipe
from .search_recipe_data import SearchRecipeData
from .values import cats_values

def search(request, keywords=''):
    context = {
        'title': 'Search',
        'recipes': '',
        'keywords': keywords,
        'counts': 0,
        'categories': [
            {
                'name_upper': 'Courses',
                'name_lower': 'courses',
                'image': 'recipe/images/recipe_course.png',
                'items': None,
            },
            {
                'name_upper': 'Diets',
                'name_lower': 'diets',
                'image': 'recipe/images/recipe_diet.png',
                'items': None,
            },
            {
                'name_upper': 'Occasions',
                'name_lower': 'occasions',
                'image': 'recipe/images/recipe_occasion.png',
                'items': None,
            }
        ]
    }

    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        context['keywords'] = keywords
        search_recipe = SearchRecipe(keywords)
        context['counts'] = search_recipe.counts
        recipe_instances = search_recipe.recipes
        context['recipes'] = [SearchRecipeData(recipe=instance).recipe_data for instance in recipe_instances]
        categories = recipes_category(context['recipes'])
        # Update the items sets to recipes categories
        for (k, v), i in zip(categories.items(), range(len(context['categories']))):
            context['categories'][i]['items'] = v
        
        # print(context['categories'])


    return render(request, 'search.html', context)


def recipes_category(recipes):
    """
    Filter category
    """
    categories = {
        'courses': {},
        'diets': {},
        'occasions': {},
    }

    for recipe in recipes:
        # Category Courses
        print(recipe)
        categories['courses'][recipe['course']] = cats_values['courses'][recipe['course']]
        # Category Diets
        if recipe['diets']:
            for diet in recipe['diets']:
                categories['diets'][diet] = cats_values['diets'][diet]
        # Category Occasions
        if recipe['occasions']: 
            for occasion in recipe['occasions']:
                categories['occasions'][occasion] = cats_values['occasions'][occasion]
    return categories
