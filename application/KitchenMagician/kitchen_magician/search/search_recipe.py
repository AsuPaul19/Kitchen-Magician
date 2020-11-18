import re
from operator import or_
from functools import reduce
from django.db.models import Q
from collections import defaultdict

# Packages for Search Bar Only
from recipe.models import Recipe
from recipe.models import RecipeInformation
from recipe.models import RecipeInstruction
from recipe.models import RecipeIngredient
from recipe.models import RecipeOccasion
from recipe.models import RecipeDiet
from recipe.models import RecipeCourse

class SearchRecipe():
    def __init__(self, keywords=None):
        self.keywords = keywords
        self.recipes = self.filter(self.keywords)
        self.counts = len(self.recipes)

    def filter(self, keywords=None):
        # Return counts and recipes
        """
        the regular expression "\s|(?<!\d)[,.](?!\d)" 
        where "\s" means to split by whitespace, 
        "(?<!\d)[,.]" means to only split by , or . 
        if it is not preceded by a digit, 
        and "[,.](?!\d)" means to only split by , 
        or . if it is not followed by a digit.
        """
        print("=" * 50)
        print(f'Before: {keywords}')
        keywords = re.split("\s|(?<!\d)[,.](?!\d)", keywords.lower())
        print(f'after: {keywords}')
        keywords = [k for k in keywords if k]
        print(f'Remove Space: {keywords}')
        search_models = self.recipe_search_models()
        recipes = defaultdict(int)
        if keywords:
            # print("=" * 80)
            # print(f'keywords: {keywords}')
            # The case insensitive search in Django
            # SELECT ... WHERE string LIKE '%keyword%';
            for model, fk in search_models.items():
                model_instances = model.objects.filter(reduce(or_, (Q(name__icontains=x) for x in keywords)))
                # If the model has a foreign key referring to recipe, get the recipe with fk
                if fk:
                    # If the model has a foreign key referring to all items, get the recipe with model_set
                    if fk['model_set']: 
                        # all modle's sets
                        model_instances = [getattr(instance, fk['model_set']).all() for instance in model_instances]
                        # get recipes from sets
                        model_instances = [instance.recipe for instances in model_instances for instance in instances]
                    else:
                        model_instances = [instance.recipe for instance in model_instances]
                # print(model_instances)
                # accumulate the appearances of recipe instances
                for instance in model_instances:
                    recipes[instance] += 1
            # print(recipes)
            # sorted by values, return keys only
            recipes = [k for k, _ in sorted(recipes.items(), key=lambda kv:kv[1], reverse=True)]
            # print(recipes)

        # Return all results if keywords is None
        else: 
            recipes = Recipe.objects.all()

        return recipes


    def recipe_search_models(self):
        # All related tables will be looked up
        search_models = {
            # Model: if having Foreign Key
            Recipe: False,
            RecipeInstruction: {
                'model_set': False
            },
            RecipeInformation: {
                'model_set': False
            },
            # Model set
            RecipeDiet: {
                'model_set': 'recipedietitem_set'
            },
            RecipeOccasion: {
                'model_set': 'recipeoccasionitem_set'
            },
            RecipeCourse: {
                'model_set': 'recipecourseitem_set'
            },
            RecipeIngredient: {
                'model_set': 'recipeingredientitem_set'
            },
        }
        # instances_diet = instance.recipedietitem_set.all()
        # for instance_diet in instances_diet:
        #     print(instance_diet.recipe_diet.name)
        return search_models