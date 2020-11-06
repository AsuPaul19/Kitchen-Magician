from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Jeff's Recipe Testing
class RecipeTest(models.Model):
    title = models.CharField(max_length=100)
    # if a user is deleted, we will the post, but the reverse doesn't hold:  one-way street
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    cover = models.ImageField(upload_to='images/')


    class Meta():
        db_table = 'search_recipetest'

    # to make output more descriptive in Python shell
    def __str__(self):
        return self.title



class RecipeUploadImageTest(models.Model):
    image_folder = 'recipe_pics/'
    image = models.ImageField(upload_to=image_folder)

    class Meta():
        db_table = 'recipe_upload_image_test'

    def __str__(self):
        return self.image

# Allen's
class Recipe(models.Model):
    # CASCADE, once the user is deleted, the recipe will be deleted automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Name')
    quantity_serve = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta():
        db_table = 'recipe'

    def __str__(self):
        return f'{self.name} by {self.user.username}'


class RecipePreparationTime(models.Model):
    preparation_time = models.CharField(max_length=20)
    preparation_time_max = models.IntegerField()
    preparation_time_min = models.IntegerField()
    class Meta():
        db_table = 'recipe_preparation_time'

    def __str__(self):
        return self.preparation_time

class RecipePreparationTimeItem(models.Model):
        # CASCADE, once the user is deleted, this item will be deleted automatically
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    preparation_time = models.ForeignKey(RecipePreparationTime, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_preparation_time_item'

    def __str__(self):
        return f'{self.preparation_time.preparation_time} - {self.recipe.name}'

class RecipeQuantityServe(models.Model):
    quantity_serve = models.CharField(max_length=8)
    quantity_serve_num = models.IntegerField()

    class Meta():
        db_table = 'recipe_quantity_serve'

    def __str__(self):
        return self.quantity_serve


class RecipeCourse(models.Model):
    name = models.CharField(default='Others', max_length=50)

    class Meta():
        db_table = 'recipe_course'

    def __str__(self):
        return self.name


class RecipeCourseItem(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    recipe_course = models.ForeignKey(RecipeCourse, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_course_item'

    def __str__(self):
        return f'{self.recipe.name} - {self.recipe_course.course}'


class RecipeIngredient(models.Model):
    name = models.CharField(max_length=100)

    class Meta():
        db_table = 'recipe_ingredient'

    def __str__(self):
        return self.name


class RecipeIngredientItem(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    recipe_ingredient = models.ForeignKey(RecipeIngredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_ingredient_item'

    def __str__(self):
        return f'{self.recipe.name} - {self.recipe_ingredient.ingredient}'


class RecipeInformation(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    name = models.CharField(max_length=500)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_information'

    def __str__(self):
        return f'{self.recipe.name} - {self.information}'


class RecipeInstruction(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    name = models.CharField(max_length=500)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_instruction'

    def __str__(self):
        return f'{self.recipe.name} - {self.instruction}'



class RecipeImage(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    image_folder = 'recipe_pics/'
    image = models.ImageField(
        default=image_folder + 'default_recipe_image.jpg', upload_to=image_folder)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_image'

    def __str__(self):
        return f'{self.recipe.name} - {self.image}'

class RecipeVideo(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    video_link = models.CharField(max_length=1000)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_video'

    def __str__(self):
        return self.recipe.name


class RecipeFavorite(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_favorite'

    def __str__(self):
        return f'{self.recipe.name} by {self.user.username}'

class RecipeUpvote(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_upvote'

    def __str__(self):
        return f'{self.recipe.name} by {self.user.username}'


class RecipeComment(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    created = models.DateTimeField(default=timezone.now)

    class Meta():
        db_table = 'recipe_comment'

    def __str__(self):
        return f'Recipe - {self.recipe.name}, User - {self.user.username}, Comment - {self.comment}'


class RecipeOccasion(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    name = models.CharField(max_length=50)

    class Meta():
        db_table = 'recipe_occasion'

    def __str__(self):
        return self.name

class RecipeOccasionItem(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    recipe_occasion = models.ForeignKey(RecipeOccasion, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_occasion_item'

    def __str__(self):
        return f'{self.occasion.name} - {self.recipe.name}'

class RecipeDiet(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    name = models.CharField(max_length=50)

    class Meta():
        db_table = 'recipe_diet'

    def __str__(self):
        return self.name

class RecipeDietItem(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    recipe_diet = models.ForeignKey(RecipeDiet, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta():
        db_table = 'recipe_diet_item'

    def __str__(self):
        return f'{self.diet.name} - {self.recipe.name}'