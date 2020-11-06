# Syntax for SHELL to update databases
# python3 manage.py shell

# Create recipe

from recipe.mysql.create_recipe import CreateRecipe
from recipe.mysql.create_recipe import test_recipe
recipe = CreateRecipe(test_recipe())
recipe.create_recipe()


# update recipe quantity serve
import recipe.mysql.updates as updates
updates.update_quantity_serve()


# update recipe preparation_time
import recipe.mysql.updates as updates
updates.update_preparation_time()

# update recipe course
import recipe.mysql.updates as updates
updates.update_course()

# update recipe occasion
import recipe.mysql.updates as updates
updates.update_occasion()

# update recipe diet
import recipe.mysql.updates as updates
updates.update_diet()