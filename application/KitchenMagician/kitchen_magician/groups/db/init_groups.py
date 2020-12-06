groups = [
        {
        "img": "groups/images/vegan.png",
        "name": "Vegan Group",
    },
    {    
        "img": "groups/images/ketogenic-diet.png",
        "name": "Keto Group",
    },       
    {
        "img": "groups/images/vegetables.png",
        "name": "Vegetarian Group",
    },
    {
        "img": "groups/images/gluten-free.png",
        "name": "Gluten Free Group",
    },
    {  
        "img": "groups/images/sushi.png",
        "name": "Raw Diet", 
    },
    {
        "img": "groups/images/sardine.png",
        "name": "Pescatarian Group",
    },   
    {
        "img": "groups/images/fruits.png",
        "name": "Paleo Group",
    },   
        
    {
        "img": "groups/images/low-carb-diet.png",
        "name": "Low Carb Group",
    }
    
]      

def initialize_groups():
    from groups.models import Group
    for group in groups:
        new_group = Group(img_path=group["img"], name=group["name"])
        new_group.save()
        print(f'Added group - {new_group.name}')