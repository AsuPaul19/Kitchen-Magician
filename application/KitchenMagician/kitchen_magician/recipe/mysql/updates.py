"""
# python3 manage.py shell
# update in mysql

from recipe.mysql import updates
updates.update_quantity_serve()
updates.update_preparation_time()
updates.update_cooking_time()
updates.update_occasion()
updates.update_course()
updates.update_diet()

"""

# Quantity Serve
def update_quantity_serve():
    from recipe.models import RecipeQuantityServe
    quantity_server = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10+': 10
    }

    for k, v in quantity_server.items():
        rqs = RecipeQuantityServe(quantity_serve=k, quantity_serve_num=v)
        rqs.save()
    
    print("Successful on RecipeQuantityServe!")


# preparation time
def update_preparation_time():
    from recipe.models import RecipePreparationTime
    quantity_prepation_time = [
        {
            'preparation_time': '00-15 min',
            'preparation_time_max': 15,
            'preparation_time_min': 10
        },
        {
            'preparation_time': '15-30 min',
            'preparation_time_max': 30,
            'preparation_time_min': 15
        },
        {
            'preparation_time': '30-60 min',
            'preparation_time_max': 60,
            'preparation_time_min': 30
        },
        {
            'preparation_time': '1-2 hours',
            'preparation_time_max': 120,
            'preparation_time_min': 60
        },
        {
            'preparation_time': '2-4 hours',
            'preparation_time_max': 240,
            'preparation_time_min': 120
        },
        {
            'preparation_time': '4+ hours',
            'preparation_time_max': 86400, # One day
            'preparation_time_min': 240
        },
    ]

    for q in quantity_prepation_time:
        rqt = RecipePreparationTime(
            preparation_time=q['preparation_time'], 
            preparation_time_max=q['preparation_time_max'],
            preparation_time_min=q['preparation_time_min']
            )
        rqt.save()
    
    print("Successful on RecipePreparationTime!")

# Recipe Cooking Time
def update_cooking_time():
    from recipe.models import RecipeCookingTime
    cooking_time = [
        {
            'cooking_time': '00-15 min',
            'cooking_time_max': 15,
            'cooking_time_min': 10
        },
        {
            'cooking_time': '15-30 min',
            'cooking_time_max': 30,
            'cooking_time_min': 15
        },
        {
            'cooking_time': '30-60 min',
            'cooking_time_max': 60,
            'cooking_time_min': 30
        },
        {
            'cooking_time': '1-2 hours',
            'cooking_time_max': 120,
            'cooking_time_min': 60
        },
        {
            'cooking_time': '2-4 hours',
            'cooking_time_max': 240,
            'cooking_time_min': 120
        },
        {
            'cooking_time': '4+ hours',
            'cooking_time_max': 86400, # One day
            'cooking_time_min': 240
        },
    ]
    for c in cooking_time:
        rct = RecipeCookingTime(
            cooking_time=c['cooking_time'], 
            cooking_time_max=c['cooking_time_max'],
            cooking_time_min=c['cooking_time_min']
            )
        rct.save()
    
    print("Successful on RecipeCookingTime!")

# recipe course
def update_course():
    from recipe.models import RecipeCourse
    course = [
        'Appetizers',
        'Beverages',
        'Breads',
        'Breakfast/Brunch',
        'Condiments',
        "Desserts",
        'Main Dishes',
        'Salads',
        'Sandwiches',
        'Side Dishes',
        'Others'
    ]

    for c in course:
        rc = RecipeCourse(name=c)
        rc.save()
    print("Successful on RecipeCourse!")

# recipe occasion/holiday
def update_occasion():
    from recipe.models import RecipeOccasion
    occasion = [
        'Chinese New Year',
        'Christmas',
        'Diwali',
        'Easter', 
        'Father’s Day',
        'Halloween',  
        'Hanukkah',  
        'Independence Day',
        'Labor Day',
        'Martin Luther King Day',
        'Memorial Day',
        'Mother’s Day',
        "New Year's",  
        'Patriotic',  
        "St. Patrick's",  
        'Super Bowl',
        'Thanksgiving',  
        "Valentine's Day",  
        "Others"
    ]

    for o in occasion:
        ro = RecipeOccasion(name=o)
        ro.save()
    print("Successful on Occasion!")


# recipe diet
def update_diet():
    from recipe.models import RecipeDiet
    diet = [
        'Vegan',
        'Keto',
        'Vegetarian',
        'Gluten Free',
        'Pescatarian',
        'Paleo',
        'Low Carb',
        'Raw',
        'Others'
    ]

    for d in diet:
        d = RecipeDiet(name=d)
        d.save()
    print("Success on Diet!")

def main():
    update_quantity_server()

if __name__ == '__mian__':
    main()