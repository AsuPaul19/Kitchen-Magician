# Generated by Django 3.1.1 on 2020-11-15 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('quantity_serve', models.IntegerField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'recipe',
            },
        ),
        migrations.CreateModel(
            name='RecipeCookingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooking_time', models.CharField(max_length=20)),
                ('cooking_time_max', models.IntegerField()),
                ('cooking_time_min', models.IntegerField()),
            ],
            options={
                'db_table': 'recipe_cooking_time',
            },
        ),
        migrations.CreateModel(
            name='RecipeCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Others', max_length=50)),
                ('image', models.ImageField(default='default_images/default_recipe_course_image.jpg', upload_to='recipe_course_pics/')),
            ],
            options={
                'db_table': 'recipe_course',
            },
        ),
        migrations.CreateModel(
            name='RecipeDiet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default_images/default_recipe_diet_image.jpg', upload_to='recipe_diet_pics/')),
            ],
            options={
                'db_table': 'recipe_diet',
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'recipe_ingredient',
            },
        ),
        migrations.CreateModel(
            name='RecipeOccasion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default_images/default_recipe_occasion_image.jpg', upload_to='recipe_occasion_pics/')),
            ],
            options={
                'db_table': 'recipe_occasion',
            },
        ),
        migrations.CreateModel(
            name='RecipePreparationTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preparation_time', models.CharField(max_length=20)),
                ('preparation_time_max', models.IntegerField()),
                ('preparation_time_min', models.IntegerField()),
            ],
            options={
                'db_table': 'recipe_preparation_time',
            },
        ),
        migrations.CreateModel(
            name='RecipeQuantityServe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_serve', models.CharField(max_length=8)),
                ('quantity_serve_num', models.IntegerField()),
            ],
            options={
                'db_table': 'recipe_quantity_serve',
            },
        ),
        migrations.CreateModel(
            name='RecipeVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_link', models.CharField(max_length=1000)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
            options={
                'db_table': 'recipe_video',
            },
        ),
        migrations.CreateModel(
            name='RecipeUpvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'recipe_upvote',
            },
        ),
        migrations.CreateModel(
            name='RecipeTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('cover', models.ImageField(upload_to='images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'search_recipetest',
            },
        ),
        migrations.CreateModel(
            name='RecipePreparationTimeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preparation_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipepreparationtime')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
            options={
                'db_table': 'recipe_preparation_time_item',
            },
        ),
        migrations.CreateModel(
            name='RecipeOccasionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
                ('recipe_occasion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipeoccasion')),
            ],
            options={
                'db_table': 'recipe_occasion_item',
            },
        ),
        migrations.CreateModel(
            name='RecipeInstruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
            options={
                'db_table': 'recipe_instruction',
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredientItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
                ('recipe_ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipeingredient')),
            ],
            options={
                'db_table': 'recipe_ingredient_item',
            },
        ),
        migrations.CreateModel(
            name='RecipeInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
            options={
                'db_table': 'recipe_information',
            },
        ),
        migrations.CreateModel(
            name='RecipeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default_images/default_recipe_image.jpg', upload_to='recipe_pics/')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
            options={
                'db_table': 'recipe_image',
            },
        ),
        migrations.CreateModel(
            name='RecipeFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'recipe_favorite',
            },
        ),
        migrations.CreateModel(
            name='RecipeDietItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
                ('recipe_diet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipediet')),
            ],
            options={
                'db_table': 'recipe_diet_item',
            },
        ),
        migrations.CreateModel(
            name='RecipeCourseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
                ('recipe_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipecourse')),
            ],
            options={
                'db_table': 'recipe_course_item',
            },
        ),
        migrations.CreateModel(
            name='RecipeCookingTimeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooking_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipecookingtime')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
            options={
                'db_table': 'recipe_cooking_time_item',
            },
        ),
        migrations.CreateModel(
            name='RecipeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'recipe_comment',
            },
        ),
    ]
