from .models import RecipeCourseItem
from .models import RecipeImage
from .models import RecipeInformation
from .models import RecipePreparationTimeItem
from .models import RecipeCookingTimeItem
from .models import RecipeVideo
from .models import RecipeIngredientItem
from .models import RecipeOccasionItem
from .models import RecipeDietItem
from .models import RecipeInstruction
from .models import Recipe
from .models import RecipeFavorite
from django.contrib.auth.models import User



"""
Return a recipe data as a dictionary
        
    recipe_data_json = {
        # Key - name:   Value   Type (name),
        'user':  String, self.username,
        'name': String, self.recipe name),
        'recipe_id': int
        'information': String, self.recipe_information(recipe),
        'ingredients': List, self.recipe_ingredients(recipe),
        'instructions': List, self.recipe_instruction(recipe),
        "images": String for image path, self.recipe_image(recipe)
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
        self.recipe = recipe  # recipe instance
        self.recipe_id = recipe_id  # recipe id
        self.is_valid = False # valid recipe instance or id 
        self.recipe_data = self.get_recipe() # recipe data

    def is_valid(self):
        # if we can fetch the recipe with its instance or id, return true
        # else return false
        # type(self.recipe==Recipe) Check the type
        return isinstance(self.recipe, Recipe) or Recipe.objects.filter(id=self.recipe_id).first()

    def get_recipe(self):
        recipe = None
        # get data with recipe instance
        if isinstance(self.recipe, Recipe): # if the instance is a <class 'Recipe'>
            recipe = self.recipe
            self.is_valid = True
        # get data with recipe id
        elif self.recipe_id:
            self.recipe = recipe = Recipe.objects.filter(id=self.recipe_id).first()
            if recipe:
                self.is_valid = True
        
        return self.recipe_data(recipe)

    def recipe_data(self, recipe):
        recipe_data_json = None
        if recipe: 
            # Collect recipe data
            user_name, user_avatar = self.recipe_user(recipe)
            recipe_data_json = {
                    'user': user_name,
                    'user_avatar': user_avatar,
                    'name': self.recipe_name(recipe),
                    'recipe_id': self.recipe.id,
                    'information': self.recipe_information(recipe),
                    'ingredients': self.recipe_ingredients(recipe),
                    'instructions': self.recipe_instruction(recipe),
                    "images": self.recipe_image(recipe),
                    "video_link": self.recipe_video_link(recipe),
                    "quantity_serve": self.recipe_quantity_serve(recipe),
                    "preparation_time": self.recipe_preparation_time(recipe), 
                    "cooking_time": self.recipe_cooking_time(recipe), 
                    "course": self.recipe_course(recipe),
                    "occasions": self.recipe_occasions(recipe),
                    "diets": self.recipe_diets(recipe),
                }
                
        print(recipe_data_json)
        return recipe_data_json

    def recipe_user(self, recipe):
        user = User.objects.filter(id=recipe.user_id).first()
        if user:
            user_name = user.username
            user_avatar = None
            try:
                user_avatar = user.profile.image
            except:
                pass
            return [user_name, user_avatar]
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
    
    def recipe_cooking_time(self, recipe):
        cooking_time = RecipeCookingTimeItem.objects.filter(recipe=recipe).first()
        if cooking_time:
            return cooking_time.cooking_time.cooking_time
        else:
            return None

    def recipe_course(self, recipe):
        course = RecipeCourseItem.objects.filter(recipe=recipe).first()
        if course:
            return course.recipe_course.name
        else: 
            return None
        # Return as a list
        # courses = RecipeCourseItem.objects.filter(recipe=recipe).first()
        # if courses:
        #     return 
        #     return [r_object.recipe_course.name for r_object in courses]
        # else:
        #     return None

    def recipe_occasions(self, recipe):
        occasions = RecipeOccasionItem.objects.filter(recipe=recipe)
        if occasions:
            return [r_object.recipe_occasion.name for r_object in occasions]
        else:
            return None

    def recipe_diets(self, recipe):
        diets = RecipeDietItem.objects.filter(recipe=recipe)
        if diets:
            return [r_object.recipe_diet for r_object in diets]
        else:
            return None
        
    def recipe_favorite(self, recipe):
        # return favorite counts
        favorites = RecipeFavorite.objects.filter(recipe=recipe)
        return len(favorites)