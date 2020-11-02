# from search.models import RecipeTemp # for python3 manage.py shell
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
# import django
# django.setup()

from ..models import Recipe
from ..models import RecipeType
from ..models import RecipeTypeItem
from ..models import RecipeIngredient
from ..models import RecipeIngredientItem
from ..models import RecipeInformation
from ..models import RecipeInstruction
from ..models import RecipeImage
from ..models import RecipeVideo
from django.contrib.auth.models import User

# Example for Testing 
def test_recipe():
    recipe = {
        "user_id": 1,
        "name": "Grilled Marinated Shrimp",
        "preparation_time": 20,
        "types": ["lunch", "dinner"],
        "information": "This makes the best shrimp! Remove from skewers and serve on a bed of pasta with sauce for a great meal.",
        "ingredients": ["shrimp", "garlic", "lemon", "butter"],
        "instructions": [
            "Heat olive oil in a heavy skillet over high heat until it just begins to smoke. Place shrimp in an even layer on the bottom of the pan and cook for 1 minute without stirring.",
            "Season shrimp with salt; cook and stir until shrimp begin to turn pink, about 1 minute.",
            "Stir in garlic and red pepper flakes; cook and stir 1 minute. Stir in lemon juice, caper brine, 1 1/2 teaspoon cold butter, and half the parsley.",
            "Cook until butter has melted, about 1 minute, then turn heat to low and stir in 1 1/2 tablespoon cold butter. Cook and stir until all butter has melted to form a thick sauce and shrimp are pink and opaque, about 2 to 3 minutes.",
            "Remove shrimp with a slotted spoon and transfer to a bowl; continue to cook butter sauce, adding water 1 teaspoon at a time if too thick, about 2 minutes. Season with salt to taste.",
            "Serve shrimp topped with the pan sauce. Garnish with remaining flat-leaf parsley."
            ],
        "images": [
            'test1.jpg',
            'test2.jpg'
            ],
        "video_link": [
            "test_video_link"
        ]
    }

    return recipe

class CreateRecipe():
    """
    Create a single recipe
    1. name

    recipes tables:
        1. recipe_type
        2. recipe_ingredient
        3. recipe_information
        4. recipe_instruction
        5. recipe_image
        6. recipe_video
    
    """
    def __init__(self, recipe):
        self.user_id = recipe['user_id']
        self.name = recipe['name']
        self.preparation_time = recipe['preparation_time']
        self.types = recipe['types']
        self.information = recipe['information']
        self.ingredients = recipe['ingredients']
        self.instructions = recipe['instructions']
        self.images = recipe['images']
        self.video_link = recipe['video_link']
        self.recipe_object = None

    # create recipe types
    def create_recipe_type(self):
        for type in self.types:
            recipe_type = RecipeType.objects.filter(type=type).first()
            # If the type is not in the database, add it to the db_table: recipe_type
            if not recipe_type:
                recipe_type = RecipeType(type=type)
                recipe_type.save()
            # create the recipe type item simultaneously
            self.create_recipe_type_item(recipe_type)

        # create recipe types items
    def create_recipe_type_item(self, recipe_type):
        recipes_types_item_object = RecipeTypeItem(recipe_type=recipe_type, recipe=self.recipe)
        recipes_types_item_object.save()

    # create recipe information
    def create_recipe_information(self):
        recipe_information = RecipeInformation(information=self.information, recipe=self.recipe)
        recipe_information.save()

            # create recipe ingredients
    def create_recipe_ingredient(self):
        for ingredient in self.ingredients:
            recipe_ingredient = RecipeIngredient.objects.filter(ingredient=ingredient).first()
            # If the ingredient is not in the database, add it to the db_table: recipe_ingredient
            if not recipe_ingredient:
                recipe_ingredient = RecipeIngredient(ingredient=ingredient)
                recipe_ingredient.save()
            # create the recipe ingredient item simultaneously
            self.create_recipe_ingredient_item(recipe_ingredient)

    # create recipe ingredients
    def create_recipe_ingredient_item(self, recipe_ingredient):
        recipe_ingredient_item = RecipeIngredientItem(recipe_ingredient=recipe_ingredient, recipe=self.recipe)
        recipe_ingredient_item.save()

        # create recipe ingredients
    def create_recipe_instruction(self):
        for instruction in self.instructions: 
            recipe_instruction = RecipeInstruction(instruction=instruction, recipe=self.recipe)
            recipe_instruction.save()

    # create recipe images
    def create_recipe_image(self):
        for image in self.images:
            recipe_image = RecipeImage(image=image, recipe=self.recipe)
            recipe_image.save()

    # create recipe images
    def create_recipe_video(self):
        recipe_video = RecipeVideo(video_link=self.video_link, recipe=self.recipe)
        recipe_video.save()

    # create recipes
    def create_recipe(self):
        self.recipe = Recipe(
                # TO-DO
                # Change it to User
                user_id=self.user_id,
                name=self.name,
                preparation_time=self.preparation_time,
            )
        self.recipe.save()
        self.create_recipe_type()
        self.create_recipe_information()
        self.create_recipe_ingredient()
        self.create_recipe_instruction()
        self.create_recipe_image()
        self.create_recipe_video()

