from recipe.models import Recipe
from recipe.models import RecipeFavorite
from recipe.models import RecipeImage


numbers_letters = [
    "first", "second", "third", "fourth", 
    "fifth", "sixth", "seventh", "eighth", 
    "ninth", "tenth", "eleventh", "twelfth"
    ]

# return top n most popular recipes
def top_recipes(n=5):
    # return recipe image and id
    # Fetch all recipes
    recipes_all = Recipe.objects.all()
    # Store each recipe as pair of (recipe, number of users)
    recipes_num = [(recipe, len(RecipeFavorite.objects.filter(recipe=recipe))) for recipe in recipes_all]
    # sort by numbers and get top n recipes
    recipes_top = sorted(recipes_num, key=lambda recipe: recipe[1], reverse=True)[:n]
    # return recipes object only
    # recipes_res = [recipe for recipe, _ in recipes_top]
    recipes = []
    for i, (recipe, _) in enumerate(recipes_top):
        recipe_image = RecipeImage.objects.filter(recipe=recipe).first()
        recipe_data = {
            "name": recipe.name,
            "image_path": recipe_image.image.url,
            "id": recipe.id,
            "alt": f'{numbers_letters[i]}-recipe'
        }
        recipes.append(recipe_data)
    return recipes




recipes_cats = [

    {
        "name": "occasion-recipes",
        "title": "Recipes by Occasion",
        "slogan": "Find the perfect recipe for any occasion. Check out the top 4 occasions.",
        "items": [
            {
                "keywords": "Christmas",
                "title": "Christmas",
                "image_path": "home/images/cats/occasion_christmas.jpg",
            },
            {
                "keywords": "Super Bowl",
                "title": "Super Bowl",
                "image_path": "home/images/cats/occasion_superbowl.jpg",
            },
            {
                "keywords": "Thanksgiving",
                "title": "Thanksgiving",
                "image_path": "home/images/cats/occasion_thanksgiving.jpg",
            },
            {
                "keywords": "New Year's",
                "title": "New Year's",
                "image_path": "home/images/cats/occasion_new-years.jpg",
            },
        ]
        
    },
    
    {
        "name": "course-recipes",
        "title": "Recipes by Course",
        "slogan": "Find the perfect recipe for any course.Check out the top 4 courses.",
        "items": [
            {
                "keywords": "Main Dishes",
                "title": "Main Dishes",
                "image_path": "home/images/cats/course_main-dishes.jpg",
            },
            {
                "keywords": "Desserts",
                "title": "Desserts",
                "image_path": "home/images/cats/course_desserts.jpg",
            },
            {
                "keywords": "Sandwiches",
                "title": "Sandwiches",
                "image_path": "home/images/cats/course_sandwiches.jpeg",
            },
            {
                "keywords": "Breakfast Brunch",
                "title": "Breakfast/Brunch",
                "image_path": "home/images/cats/course_breakfast.jpg",
            }
        ]
        
    }
]
