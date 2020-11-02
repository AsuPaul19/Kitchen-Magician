from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Jeff's
class RecipeTest(models.Model):
    title = models.CharField(max_length=100)
    # if a user is deleted, we will the post, but the reverse doesn't hold:  one-way street
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    cover = models.ImageField(upload_to='images/')

    # to make output more descriptive in Python shell
    def __str__(self):
        return self.title


class Recipe(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Name')
    # we store time as minutes. convert it to hours : minutes when we use it
    preparation_time = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta():
        db_table = 'recipe'

    def __str__(self):
        return f'{self.name} by {self.user.username}'


class RecipeType(models.Model):
    type = models.CharField(max_length=50)

    class Meta():
        db_table = 'recipe_type'

    def __str__(self):
        return self.type


class RecipeTypeItem(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipe_type = models.ForeignKey(RecipeType, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_type_item'

    def __str__(self):
        return f'{self.recipe.name} - {self.recipe_type.type}'


class RecipeIngredient(models.Model):
    ingredient = models.CharField(max_length=100)

    class Meta():
        db_table = 'recipe_ingredient'

    def __str__(self):
        return self.ingredient


class RecipeIngredientItem(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipe_ingredient = models.ForeignKey(
        RecipeIngredient, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_ingredient_item'

    def __str__(self):
        return f'{self.recipe.name} - {self.recipe_ingredient.ingredient}'


class RecipeInformation(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically
    information = models.CharField(max_length=500)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_information'

    def __str__(self):
        return f'{self.recipe.name} - {self.information}'


class RecipeInstruction(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically
    instruction = models.CharField(max_length=500)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_instruction'

    def __str__(self):
        return f'{self.recipe.name} - {self.instruction}'


class RecipeVideo(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically
    video_link = models.CharField(max_length=1000)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_video'

    def __str__(self):
        return self.recipe.name


class RecipeImage(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically
    image_folder = 'recipe_pics/'
    image = models.ImageField(
        default=image_folder + 'default_recipe_image.jpg', upload_to=image_folder)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_image'

    def __str__(self):
        return f'{self.recipe.name} - {self.image}'
