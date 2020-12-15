from django.shortcuts import render
from home.db.recipes_data import recipes_cats
from home.db.groups_data import top_groups
from search.popular_search import popular_search

# Create your views here.


trending_recipes = [
    {
        "img": "home/images/slider/K2O.jpg"
    },
    {
        "img": "home/images/slider/K3O.jpg"
    },
        {
        "img": "home/images/slider/K4O.jpg"
    },
        {
        "img": "home/images/slider/K5O.jpg"
    }
]

trending_recipes_carousel = [
    {
        "img": "home/images/slider/K2O.jpg",
        "alt": "k20"
    },
    {
        "img": "home/images/slider/K3O.jpg",
        "alt": "k30"
    },
        {
        "img": "home/images/slider/K4O.jpg",
        "alt": "k40"
    },
        {
        "img": "home/images/slider/K5O.jpg",
        "alt": "K50"
    }
]

def home(request):
    context = {
        "popular_search_keywords": popular_search(5), # top5 search
        "trending_recipes": trending_recipes,
        "trending_recipes_carousel": trending_recipes_carousel,
        "recipes_cats": recipes_cats,
        "top_groups": top_groups(4), # Top 4 Most popular groups
    }

    return render(request, 'home.html', context)

def contact(request):
    context = { 
        "title": "CONTACT US"
    }

    return render(request, 'contact.html', context)

def test(request):
    return render(request, 'notes/test.html', {'title': 'Test'})




# groups = [
#     {
#         "group": "Vegan Group",
#         "img": "home/images/groups/vegan.jpg",   
#     },
#     {
#         "group": "Keto Group",
#         "img": "home/images/groups/keto.jpg",   
#     },
#     {
#         "group": "Vegetarian Group",
#         "img": "home/images/groups/vegetarian.jpg",   
#     },
#     {
#         "group": "Gluten Free Group",
#         "img": "home/images/groups/gluten-free.jpg",   
#     },
#     {
#         "group": "Pescatarian Group",
#         "img": "home/images/groups/pescatarian.jpg",   
#     },
#     {
#         "group": "Paleo Group",
#         "img": "home/images/groups/paleo.jpg",   
#     },
#     {
#         "group": "Low Carb Group",
#         "img": "home/images/groups/low-carb.jpg",   
#     },
#     {
#         "group": "Raw Group",
#         "img": "home/images/groups/raw.jpg",
#     },
# ]