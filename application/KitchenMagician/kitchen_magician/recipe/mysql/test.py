# python3 manage.py shell

# Create recipe
from recipe.mysql.create_recipe import CreateRecipe
from recipe.mysql.create_recipe import test_recipe
recipe = CreateRecipe(test_recipe())
recipe.create_recipe()

# Add recipe types