from django.core.files.storage import FileSystemStorage
from .models import RecipeCourseItem
from .models import RecipeImage
from .models import RecipeInformation
from .models import RecipePreparationTimeItem
from .models import RecipeVideo
from .models import RecipeIngredientItem
from .models import RecipeOccasionItem
from .models import RecipeDietItem
from .models import RecipeInstruction
from .models import Recipe
from django.contrib.auth.models import User



"""
Return a recipe data as a dictionary
        
    recipe_data_json = {
        # Key - name:   Value -  Type (name)
        'user':  String (username)
        'name': String (recipe name),
        'information': String (),
        'ingredients': self.recipe_ingredients(recipe),
        'instructions': self.recipe_instruction(recipe),
        "images": self.recipe_image(recipe)
        "video_link": RecipeVideo.objects.filter(recipe=recipe).first().video_link,
        "quantity_serve": recipe.quantity_serve,
        "preparation_time": RecipePreparationTimeItem.objects.filter(recipe=recipe).first().preparation_time.preparation_time,
        "courses": [r_object.recipe_course.name for r_object in RecipeCourseItem.objects.filter(recipe=recipe)],
        "occasions": [r_object.recipe_occasion.name for r_object in RecipeOccasionItem.objects.filter(recipe=recipe)],
        "diets": [r_object.recipe_diet.name for r_object in RecipeDietItem.objects.filter(recipe=recipe)],
    }

"""


class RecipeDataFetch():
    def __init__(self, recipe=None, recipe_id=None):
        self.recipe = recipe
        self.recipe_id = recipe_id

    def get_recipe(self):
        recipe = None
        # get data with recipe instance
        if self.recipe:
            recipe = self.recipe
        # get data with recipe id
        elif self.recipe_id:
            recipe = Recipe.objects.filter(id=self.recipe_id)
        
        return self.recipe_data(recipe)



    def recipe_data(self, recipe):
        # Collect recipe data
        recipe_data_json = {
                'user': self.recipe_user(recipe),
                'name': self.recipe_name(recipe),
                'information': self.recipe_information(recipe),
                'ingredients': self.recipe_ingredients(recipe),
                'instructions': self.recipe_instruction(recipe),
                "images": self.recipe_image(recipe),
                "video_link": self.recipe_video_link(recipe),
                "quantity_serve": self.recipe_quantity_serve(recipe),
                "preparation_time": self.recipe_preparation_time(recipe), 
                "courses": self.recipe_courses(recipe),
                "occasions": self.recipe_occasions(recipe),
                "diets": self.recipe_diets(recipe),
            }
        print(recipe_data_json)
        return recipe_data_json

    def recipe_user(self, recipe):
        if recipe.user:
            return recipe.user.username
        else:
            return None

    def recipe_name(self, recipe):
        return recipe.name

    def recipe_information(self, recipe):
        information = RecipeInformation.objects.filter(recipe=recipe).first()
        if information:
            return information.name
        else:
            return None
    
    def recipe_ingredients(self, recipe):
        ingredients_items = RecipeIngredientItem.objects.filter(recipe=recipe)
        if ingredients_items:
            return [r_object.recipe_ingredient.name for r_object in ingredients_items]
        else:
            return None
    
    def recipe_instruction(self, recipe):
        instructions = RecipeInstruction.objects.filter(recipe=recipe)
        if instructions:
            return [r_object.name for r_object in instructions]
        else:
            return None

    def recipe_image(self, recipe):
        image = RecipeImage.objects.filter(recipe=recipe).first()
        if image:
            return image.image
        else:
            return None

    def recipe_video_link(self, recipe):
        video_link = RecipeVideo.objects.filter(recipe=recipe).first()
        if video_link:
            return video_link.video_link
        else:
            return None

    def recipe_quantity_serve(self, recipe):
        return recipe.quantity_serve

    def recipe_preparation_time(self, recipe):
        preparation_time = RecipePreparationTimeItem.objects.filter(recipe=recipe).first()
        if preparation_time:
            return preparation_time.preparation_time.preparation_time
        else:
            return None

    def recipe_courses(self, recipe):
        courses = RecipeCourseItem.objects.filter(recipe=recipe)
        if courses:
            return [r_object.recipe_course.name for r_object in courses]
        else:
            return None

    def recipe_occasions(self, recipe):
        occasions = RecipeOccasionItem.objects.filter(recipe=recipe)
        if occasions:
            return [r_object.recipe_occasion.name for r_object in occasions]
        else:
            return None

    def recipe_diets(self, recipe):
        diets = RecipeDietItem.objects.filter(recipe=recipe)
        if diets:
            return [r_object.recipe_diet.name for r_object in diets]
        else:
            return None
        