# python3 manage.py shell




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
        'Other'
    ]

    for c in course:
        rc = RecipeCourse(course=c)
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
        "none"
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
        'Raw'
    ]

    for d in diet:
        d = RecipeDiet(name=d)
        d.save()
    print("Success on Diet!")

def main():
    update_quantity_server()

if __name__ == '__mian__':
    main()