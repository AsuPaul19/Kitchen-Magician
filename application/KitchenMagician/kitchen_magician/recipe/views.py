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

def recipe(request):
    context = {
        'title': 'RECIPE'
    }
    return render(request, 'recipe.html', context)


# Create recipe 
def create_recipe(request):
    if request.user.is_authenticated: # authenticated user can create recipe
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
def submit_recipe(request):
    recipe = None
    if request.method == 'POST':
        data_dict = request.POST.getlist('recipe-occasion')
        print(data_dict)
        recipe = create_recipe_data(request)
    # Testing when creating recipe
    context = {
        'title': 'SUBMIT RECIPES',
        'name': recipe.name,
        'information': RecipeInformation.objects.filter(recipe=recipe).first().name,
        'ingredients': [r_object.recipe_ingredient.name for r_object in RecipeIngredientItem.objects.filter(recipe=recipe)],
        'instructions': [r_object.name for r_object in RecipeInstruction.objects.filter(recipe=recipe)],
        "images": RecipeImage.objects.filter(recipe=recipe).first().image,
        "video_link": RecipeVideo.objects.filter(recipe=recipe).first().video_link,
        "quantity_serve": recipe.quantity_serve,
        "preparation_time": RecipePreparationTimeItem.objects.filter(recipe=recipe).first().preparation_time.preparation_time,
        "courses": [r_object.recipe_course.name for r_object in RecipeCourseItem.objects.filter(recipe=recipe)],
        "occasions": [r_object.recipe_occasion.name for r_object in RecipeOccasionItem.objects.filter(recipe=recipe)],
        "diets": [r_object.recipe_diet.name for r_object in RecipeDietItem.objects.filter(recipe=recipe)],
    }
    return render(request, 'submit_success.html', context)

def create_recipe_data(request):
    data = request.POST
    print(data)
    recipe = {}
    # parse data and send to models
    try:
        uploaded_file = request.FILES['recipe-image']
        # print(uploaded_file.size)
        # print(uploaded_file.name)
        # recipe_image = RecipeUploadImageTest(image=uploaded_file)
        # recipe_image.save()
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
        for k,v in recipe.items():
            print(f'{k}: {v}')

    except Exception as e: 
        print(e)

    if recipe:
        # try:
        create_recipe = CreateRecipe(recipe)
        create_recipe.create_recipe()
        # except Exception as e: 
        #     print(e)
        print(create_recipe.recipe)
        return create_recipe.recipe
    else:
        return recipe
    
	





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

