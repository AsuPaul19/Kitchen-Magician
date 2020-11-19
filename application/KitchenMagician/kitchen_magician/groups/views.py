# from django.shortcuts import render

# # Create your views here.
# def groups(request):
#     context = {
#         'title': 'GROUPS'
#     }
#     return render(request, 'groups/groups.html', context)

#above is original 
#below is code that is attatched to groups.html


from django.shortcuts import render
from django.http import HttpResponse

team = {
    "1001": {
        "id": "1001",
        "img": "groups/images/veganclipart.jpg",
        "name": "Vegan Group",
       
       
    },
    "1002": {
        "id": "1002",
        "img": "groups/images/ketoclipart.jpg",
        "name": "Keto Group",
      
        
        
    },
    "1003": {
        "id": "1003",
         "img": "groups/images/vegdiet.png",
        "name": "Vegetarian Group",

       
    },
    "1004": {
        "id": "1004",
          "img": "groups/images/glutenn.jpg",
        "name": "Gluten Free Group",
   
        
    },
   
    "1005": {
        "id": "1005",
          "img": "groups/images/rawdiet.png",
        "name": "Raw Diet", 

        
    },

    "1006": {
        "id": "1006",
          "img": "groups/images/fishdiet.png",
        "name": "Pescatarian Group",
     
    },

"1007": {
        "id": "1007",
          "img": "groups/images/paleodiet .png",
        "name": "Paleo Group",
    
        
    }, 

    "1008": {
        "id": "1008",
         "img": "groups/images/lowcarbdiet.jpg",
        "name": "Low Carb Group",
       
       
    },



}

def groups(request):
    content = {
        "title": "Groups",
        "team": team,
    }
    return render(request, 'groups/groups.html', content)
    
def group_forum(request):
    context = {
        'title': 'GROUPS_FORUM'
    }
    return render(request, 'groups/group_forum.html', context)

def profile(request, name, id):
    content = {
        "title": team[id]["name"], 
        "profile": team[id]
    }
    return render(request, 'profile.html', content)

