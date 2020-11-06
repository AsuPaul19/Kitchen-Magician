# from search.models import RecipeTemp # for python3 manage.py shell
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
# import django
# django.setup()

from recipe.models import Recipe
from recipe.models import RecipeIngredient
from recipe.models import RecipeIngredientItem
from recipe.models import RecipeInformation
from recipe.models import RecipeInstruction
from recipe.models import RecipeImage
from recipe.models import RecipeVideo
from recipe.models import RecipePreparationTime
from recipe.models import RecipePreparationTimeItem
from recipe.models import RecipeCourse
from recipe.models import RecipeCourseItem
from recipe.models import RecipeOccasion
from recipe.models import RecipeOccasionItem
from recipe.models import RecipeDiet
from recipe.models import RecipeDietItem
from django.contrib.auth.models import User

# Example for Testing 
def test_recipe():
    # Add more items:
    # Change type to course
    # preperation time
    # quantity serve
    # change information, instruction to name

    recipe = {
        "user_id": 1,
        "name": "Grilled Marinated Shrimp",
        "preparation_time": 20,
        "types": ["Main Dishes", "Breakfast/Brunch"],
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
        1. recipe_information
        2. recipe_ingredient
            recipe_ingredient_item
        3. recipe_instruction
        4. recipe_image
        5. recipe_video
        6. recipe_quantity_serve
        7. recipe_paraperation_time
            recipe_paraperation_time_item
        8. recipe_course
            recipe_course_item
        9. recipe_occasion
            recipe_occasion_item
        10. recipe_diet
            recipe_occasion_item


        recipe = {
            "user_id": request.user,
            "name": data['recipe-name'],
            "information": data['recipe-information'],
            "ingredients": data['recipe-ingredient'],
            "instructions": data['recipe-instruction'],
            "images": [uploaded_file],
            "video_link": data['recipe-video-link'],
            "quantity_serve": data['recipe-quantity-serve'],
            "preparation_time": data['recipe-preparation-time'],
            "courses": data['recipe-course'],
            "occasions": data['recipe-occasion'],
            "diets": data['recipe-diet'],
        }
    
    """
    def __init__(self, recipe):
        self.user = recipe['user']
        self.name = recipe['name']
        self.information = recipe['information']
        self.ingredients = recipe['ingredients']
        self.instructions = recipe['instructions']
        self.images = recipe['images']
        self.video_link = recipe['video_link']
        self.quantity_serve = recipe['quantity_serve']  # id
        self.preparation_time = recipe['preparation_time'] # id
        self.courses = recipe['courses'] # id
        self.occasions = recipe['occasions'] # id
        self.diets = recipe['diets'] # id
        self.recipe = recipe

    # create recipes
    def create_recipe(self):
        self.recipe = Recipe(
                user=self.user,
                name=self.name,
                quantity_serve=self.quantity_serve[0], # store quantity_serve_num as quantity_serve
            )
        self.recipe.save()
        print("Created recipe!!")
        self.create_recipe_information()
        self.create_recipe_ingredient()
        self.create_recipe_instruction()
        self.create_recipe_image()
        self.create_recipe_video()
        self.create_preparation_time_item()
        self.create_recipe_course_item()
        self.create_recipe_occasion_item()
        self.create_recipe_diet_item()

    # create recipe information
    def create_recipe_information(self):
        recipe_information = RecipeInformation(name=self.information, recipe=self.recipe)
        recipe_information.save()
        print("create_recipe_information CREATED!")


    # create recipe ingredients
    def create_recipe_ingredient(self):
        if self.ingredients:
            for ingredient in self.ingredients:
                recipe_ingredient = RecipeIngredient.objects.filter(name=ingredient).first()
                # If the ingredient is not in the database, add it to the db_table: recipe_ingredient
                if not recipe_ingredient:
                    recipe_ingredient = RecipeIngredient(name=ingredient)
                    recipe_ingredient.save()
                    print("create_recipe_ingredient CREATED!")
                    
                # create the recipe ingredient item simultaneously
                self.create_recipe_ingredient_item(recipe_ingredient)

    # create recipe ingredients items
    def create_recipe_ingredient_item(self, recipe_ingredient):
        recipe_ingredient_item = RecipeIngredientItem(recipe_ingredient=recipe_ingredient, recipe=self.recipe)
        recipe_ingredient_item.save()
        print("create_recipe_ingredient_item CREATED!")


        # create recipe instruction
    def create_recipe_instruction(self):
        if self.instructions: 
            for instruction in self.instructions: 
                recipe_instruction = RecipeInstruction(name=instruction, recipe=self.recipe)
                recipe_instruction.save()
                print("create_recipe_instruction CREATED!")

    # create recipe images
    def create_recipe_image(self):
        if self.images: 
            for image in self.images:
                recipe_image = RecipeImage(image=image, recipe=self.recipe)
                recipe_image.save()
                print("create_recipe_image CREATED!")

    # create recipe images
    def create_recipe_video(self):
        if self.video_link: 
            recipe_video = RecipeVideo(video_link=self.video_link, recipe=self.recipe)
            recipe_video.save()
            print("create_recipe_video CREATED!")


    # create recipe quantity_serve
    # store in the table of recipe  
    
    # create recipe preparation_time_item
    def create_preparation_time_item(self):
        preparation_time_id = self.preparation_time[0]
        if preparation_time_id:
            recipe_preparation_time = RecipePreparationTimeItem(preparation_time=RecipePreparationTime.objects.filter(id=preparation_time_id).first(), recipe=self.recipe)
            recipe_preparation_time.save()    
            print("create_preparation_time_item CREATED!")


    # create recipe course item
    def create_recipe_course_item(self):
        if self.courses:
            for course_id in self.courses:
                recipe_course_item_object = RecipeCourseItem(recipe_course=RecipeCourse.objects.filter(id=course_id).first(), recipe=self.recipe)
                recipe_course_item_object.save()
                print("create_recipe_course_item CREATED!")


    # create recipe course item
    def create_recipe_occasion_item(self):
        if self.occasions:
            for occasion_id in self.occasions:
                recipe_occasion_item_object = RecipeOccasionItem(recipe_occasion=RecipeOccasion.objects.filter(id=occasion_id).first(), recipe=self.recipe)
                recipe_occasion_item_object.save()
                print("create_recipe_occasion_item CREATED!")


        # create recipe diet item
    def create_recipe_diet_item(self):
        if self.diets:
            for diet_id in self.diets:
                recipe_diet_item_object = RecipeDietItem(recipe_diet=RecipeDiet.objects.filter(id=diet_id).first(), recipe=self.recipe)
                recipe_diet_item_object.save()
                print("create_recipe_diet_item CREATED!")





