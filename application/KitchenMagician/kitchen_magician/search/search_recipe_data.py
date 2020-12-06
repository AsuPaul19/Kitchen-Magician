from django.contrib.auth.models import User
import re
from operator import or_
from functools import reduce
from django.db.models import Q
from collections import defaultdict
from .values import cats_values
# Packages for Search Bar Only
from recipe.models import Recipe
from recipe.recipe_data_fetch import RecipeDataFetch

class SearchRecipeData(RecipeDataFetch):
    def __init__(self, recipe=None, recipe_id=None):
        self.recipe = recipe  # recipe instance
        self.recipe_id = recipe_id  # recipe id
        self.is_valid = False # valid recipe instance or id 
        self.recipe_data = self.get_recipe() # recipe data

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
            # Collect recipe data for search results
            course = self.recipe_course(recipe)
            occasions = self.recipe_occasions(recipe)
            diets = self.recipe_diets(recipe)
            recipe_data_json = {
                    'name': self.recipe_name(recipe),
                    'recipe_id': self.recipe.id,
                    "images": self.recipe_image(recipe),
                    "quantity_serve": self.recipe_quantity_serve(recipe),
                    "preparation_time": self.recipe_preparation_time(recipe), 
                    "cooking_time": self.recipe_cooking_time(recipe), 
                    "course": course,
                    "course_value": self.course_dict(course),
                    "occasions": occasions,
                    "occasion_value": self.occasion_dict(occasions),
                    "diets": diets,
                    "diet_value": self.diet_dict(diets),
                    "favorites": self.recipe_favorite(recipe),
                    "max_favorites": range(min(self.recipe_favorite(recipe), 5))  # max hearts is 5
                }
                
        # print(recipe_data_json)
        return recipe_data_json

    def course_dict(self, course):
        res = ''
        if course:
            res = cats_values['courses'][course]
        return res
    
    def diet_dict(self, diets):
        # combine all diets as a string with spaces
        res = ''
        if diets:
            for diet in diets:
                print(diet.name)
                res += cats_values['diets'][diet.name] + ' '
        return res
    
    def occasion_dict(self, occasions):
        # combine all occasions as a string with spaces
        res = ''
        if occasions:
            for occasion in occasions:
                res += cats_values['occasions'][occasion] + ' '
        return res