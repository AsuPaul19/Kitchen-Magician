from .recipe_ingredient import UpdateRecipeIngredient


def main():
    recipe_ingredient = UpdateRecipeIngredient("olive")
    recipe_ingredient.update_recipe_ingredient()

if __name__ == '__main__':
    main()