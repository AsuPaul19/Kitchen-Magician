# Generated by Django 3.1.2 on 2020-11-06 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20201105_2258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipedietitem',
            old_name='recipe',
            new_name='recipe_diet',
        ),
        migrations.RenameField(
            model_name='recipeoccasionitem',
            old_name='recipe',
            new_name='recipe_occasion',
        ),
    ]