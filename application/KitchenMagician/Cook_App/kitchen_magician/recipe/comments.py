"""
GetRecipeComments
# 1. user
# 2. user_avatar
# 3. comment
# 4. created

GetGroupComments

"""


from recipe.models import RecipeComment
from .models import Recipe
from django.contrib.auth.models import User

class GetRecipeComments():
    def __init__(self, recipe=None, recipe_id=None):
        self.recipe = recipe
        self.recipe_id = recipe_id
        self.is_valid = False # valid recipe instance or id 
        self.comments = self.get_comments()

    def is_valid(self):
        # if we can fetch the recipe with its instance or id, return true
        # else return false
        # type(self.recipe==Recipe) Check the type
        return isinstance(self.recipe, Recipe) or Recipe.objects.filter(id=self.recipe_id).first()

    def get_comments(self):
        recipe = None
        # get data with recipe instance
        if isinstance(self.recipe, Recipe): # if the instance is a <class 'Recipe'>
            recipe = self.recipe
            self.is_valid = True
        # get data with recipe id
        elif self.recipe_id:
            recipe = Recipe.objects.filter(id=self.recipe_id).first()
            if recipe:
                self.is_valid = True
        
        return self.comments(recipe)

    def comments(self, recipe=None):
        comments_data = []
        all_comments = RecipeComment.objects.filter(recipe=recipe)
        if all_comments:
            for comment in all_comments:
                comments_data.append(
                    {
                        'user': comment.user.username,
                        'user_avatar': comment.user.profile.image,
                        'comment': comment.comment,
                        'created': comment.created
                    }
                )

        return comments_data
