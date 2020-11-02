from ..models import Recipe
from ..models import RecipeIngredient
from ..models import RecipeIngredientItem
from django.contrib.auth.models import User

class UpdateRecipeIngredient():
    def __init__(self, ingredient):
        self.ingredient = ingredient
        self.recipes_ingredient_object = None # Database object

    # TO-DO 
    # If ingredient is a list, use for loop to store them.
    def update_recipe_ingredient(self):
        self.recipes_ingredient_object = RecipeIngredient.objects.filter(ingredient=self.ingredient).first()
        
        # If the ingredient is not in the table recipes_ingredients, add it to the database
        if not self.recipe_ingredient_object:
            self.recipe_ingredient_object = RecipeIngredient(ingredient=self.ingredient)
            self.recipe_ingredient_object.save()
        return self.recipe_ingredient_object.id
        


class UpdateRecipeIngredientItem():
    def __init__(self, ingredient):
        self.ingredient = ingredient
        self.recipe_ingredient_object = None # Database object
