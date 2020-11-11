from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import RecipeCourseItem, RecipeImage, RecipeInformation, RecipeIngredient, RecipePreparationTimeItem, RecipeUploadImageTest, RecipeVideo
from .models import RecipeDiet
from .models import RecipeOccasion
from .models import RecipeCourse
from .models import RecipeQuantityServe
from .models import RecipePreparationTime
from .models import RecipeIngredientItem
from .models import RecipeOccasionItem
from .models import RecipeDietItem
from .models import RecipeInstruction
from django.conf import settings
from .mysql.create_recipe import CreateRecipe
from .recipe_data_fetch import RecipeDataFetch

def recipe(request, recipe=None, recipe_id=None):
    context = {
            'title': 'SUBMIT RECIPES',
            'recipe': None,
        }

    # fetch recipe with either recipe instance or recipe id recipe_id
    recipe_data_fetch = None
    if recipe:
        recipe_data_fetch = RecipeDataFetch(recipe=recipe)
    elif recipe_id:
        recipe_data_fetch = RecipeDataFetch(recipe_id=recipe_id)

    # if we fetch the data successfully, update context and send to client
    if recipe_data_fetch:
        recipe_data = recipe_data_fetch.get_recipe()
        context['recipe'] = recipe_data
    return render(request, 'recipe.html', context)


# Create recipe page
@login_required
def create_recipe(request):
    if request.user.is_authenticated: # Only authenticated user can create recipe
        print(request.user)
    context = {
        'title': 'CREATE RECIPES',
        'diets': RecipeDiet.objects.all(),
        'courses': RecipeCourse.objects.all(),
        'occasions': RecipeOccasion.objects.all(),
        'preparation_time': RecipePreparationTime.objects.all(),
        'quantity_serve': RecipeQuantityServe.objects.all(),
    }

    return render(request, 'create_recipe.html', context)


# handle recipe submission
@login_required
def submit_recipe(request, recipe=None, recipe_id=None):
    context = {
            'title': 'SUBMIT RECIPES',
            'recipe': None,
        }
    
    # add recipe to table Recipe
    if request.method == 'POST':
        recipe = create_recipe_data(request)

    # fetch recipe with either recipe instance or recipe id recipe_id
    recipe_data_fetch = None
    if recipe:
        recipe_data_fetch = RecipeDataFetch(recipe=recipe)
    elif recipe_id:
        recipe_data_fetch = RecipeDataFetch(recipe_id=recipe_id)

    # if we fetch the data successfully, update context and send to client
    if recipe_data_fetch:
        recipe_data = recipe_data_fetch.get_recipe()
        context['recipe'] = recipe_data

    recipe(recipe, recipe_id)
    # return render(request, 'submit_success.html', context)


def create_recipe_data(request):
    data = request.POST
    recipe = {}
    # Upload Image
    try:
        uploaded_file = request.FILES['recipe-image']
        # get the size and name of the image
        # print(uploaded_file.size)
        # print(uploaded_file.name)

        # Directly store image to table
        # recipe_image = RecipeUploadImageTest(image=uploaded_file)
        # recipe_image.save()

    except Exception as e: 
        print(e)
        uploaded_file = None

    # parse data and send to models
    recipe = {
        "user": request.user,
        "name": data.getlist('recipe-name')[0],
        "information": data.getlist('recipe-information')[0],
        "ingredients": data.getlist('recipe-ingredient')[0].splitlines(),
        "instructions": data.getlist('recipe-instruction')[0].splitlines(),
        "images": [uploaded_file],
        "video_link": data.getlist('recipe-video-link')[0],
        "quantity_serve": data.getlist('recipe-quantity-serve'),
        "preparation_time": data.getlist('recipe-preparation-time'),
        "courses": data.getlist('recipe-course'),
        "occasions": data.getlist('recipe-occasion'),
        "diets": data.getlist('recipe-diet'),
    }
    # Print input data
    for k,v in recipe.items():
        print(f'{k}: {v}')

    if recipe:
        # try:
        # CreateRecipe class
        create_recipe = CreateRecipe(recipe)
        create_recipe.create_recipe()
        # except Exception as e: 
        #     print(e)
        print(create_recipe.recipe)
        return create_recipe.recipe
    else:
        return recipe
    
	

def not_found(request):
    context = {
        'title': '404 NOT FOUND'
    }
    return render(request, '404.html', context)






# Testing only 
def submit_success(request):
    context = {
        'title': 'SUCCESS'
    }
    return render(request, 'submit_success.html', context)


def upload_test(request):
    context = {
        'title': 'UPLOAD TEST'
    }
    if request.method == 'POST':
        data = request.POST
        print(data)
        print(request.FILES)
        uploaded_file = request.FILES['recipe-image']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        image = RecipeUploadImageTest(image=uploaded_file)
        image.save()
        print(uploaded_file.size)
        print(uploaded_file.name)
    return render(request, 'upload_test.html', context)

