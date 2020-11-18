from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
# from .models import RecipeUploadImageTest
from .models import RecipeDiet
from .models import RecipeOccasion
from .models import RecipeCourse
from .models import RecipeQuantityServe
from .models import RecipePreparationTime
from .models import RecipeCookingTime
from .models import RecipeComment
from .models import Recipe
from .models import RecipeFavorite
# from django.conf import settings
from .mysql.create_recipe import CreateRecipe
from .recipe_data_fetch import RecipeDataFetch
from recipe.comments import GetRecipeComments


def recipe_view(request, recipe=None, recipe_id=None):
    context = {
            'title': 'RECIPES',
            'recipe_data': None,
            'favorite': None,
        }
    # Submit new comment
    if request.method == 'POST':
        if request.user.is_authenticated:
            # POST for Add comment
            comment = request.POST.get('comment', False)
            if comment:
                new_comment = RecipeComment(user=request.user, 
                                            recipe=Recipe.objects.filter(id=recipe_id).first(), 
                                            comment=comment)
                new_comment.save()
            # POST for Change favorite
            if request.POST.get('favoriteValue', False):
                return change_favorite(user=request.user, recipe=Recipe.objects.filter(id=recipe_id).first())

    recipe_instance = RecipeDataFetch(recipe=recipe, recipe_id=recipe_id)
    # if we fetch the data successfully, send to clients
    if recipe_instance.is_valid:  
        recipe_data = recipe_instance.recipe_data
        context['recipe_data'] = recipe_data # all info for this recipe
        context['comments'] =  GetRecipeComments(recipe=recipe, recipe_id=recipe_id).comments# all info for this recipe
        if request.user.is_authenticated:
            context['favorite'] = RecipeFavorite.objects.filter(user=request.user, recipe=Recipe.objects.filter(id=recipe_id).first()).first() 
        return render(request, 'recipe.html', context)
    else: #return 404 Page if the recipe doesn't match in the database
        return not_found(request)  

def change_favorite(user=None, recipe=None):
    favorite = RecipeFavorite.objects.filter(user=user, recipe=recipe).first()
    if favorite:
        favorite.delete()
    else:
        favorite = RecipeFavorite(user=user, recipe=recipe)
        favorite.save()
    return HttpResponse("Changed favorite!")


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
        'cooking_time': RecipeCookingTime.objects.all(),
        'quantity_serve': RecipeQuantityServe.objects.all(),
    }

    return render(request, 'create_recipe.html', context)


# handle recipe submission
@login_required
def submit_recipe(request, recipe=None, recipe_id=None):
    # context = {
    #         'title': 'SUBMIT RECIPES',
    #         'recipe': None,
    #     }
    
    # add recipe to table Recipe
    if request.method == 'POST':
        recipe = create_recipe_data(request)
        # TODO redirect to recipe page
        # redirect('recipe', recipe_id=recipe.id)
    return recipe_view(request, recipe=recipe)


def create_recipe_data(request):
    data = request.POST
    recipe = None
    # Upload Image
    try:
        uploaded_file = request.FILES['recipe-image']
        # get the size and name of the image
        # print(uploaded_file.size)
        # print(uploaded_file.name)

        # Directly store image to table
        # recipe_image = RecipeUploadImageTest(image=uploaded_file)
        # recipe_image.save()
            # parse data and send to models
        submit_recipe = {
            "user": request.user,
            "name": data.getlist('recipe-name')[0],
            "information": data.getlist('recipe-information')[0],
            "ingredients": data.getlist('recipe-ingredient')[0].splitlines(),
            "instructions": data.getlist('recipe-instruction')[0].splitlines(),
            "images": [uploaded_file],
            "video_link": data.getlist('recipe-video-link')[0],
            "quantity_serve": data.getlist('recipe-quantity-serve'),
            "preparation_time": data.getlist('recipe-preparation-time'),
            "cooking_time": data.getlist('recipe-cooking-time'),
            "courses": data.getlist('recipe-course'),
            "occasions": data.getlist('recipe-occasion'),
            "diets": data.getlist('recipe-diet'),
        }
        # Print input data
        for k,v in recipe.items():
            print(f'{k}: {v}')

    except Exception as e: 
        print(e)
        uploaded_file = None

    if recipe:
        try:
            # CreateRecipe class
            create_recipe = CreateRecipe(recipe)
            create_recipe.create_recipe()
            print(create_recipe.recipe)
            return create_recipe.recipe

        except Exception as e: 
            print(e)
            return None
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


# def upload_test(request):
#     context = {
#         'title': 'UPLOAD TEST'
#     }
#     if request.method == 'POST':
#         data = request.POST
#         print(data)
#         print(request.FILES)
#         uploaded_file = request.FILES['recipe-image']
#         fs = FileSystemStorage()
#         fs.save(uploaded_file.name, uploaded_file)
#         image = RecipeUploadImageTest(image=uploaded_file)
#         image.save()
#         print(uploaded_file.size)
#         print(uploaded_file.name)
#     return render(request, 'upload_test.html', context)

