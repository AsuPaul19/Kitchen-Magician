from django.shortcuts import render
from django.http import HttpResponse

team = {
    "1001": {
        "id": "1001",
        "img": "about/images/team/1NP.jpg",
        "name": "Nicole Pang",
        "title": "Team Lead",
        "intro": [ 
            "Nicole Pang is a fourth year undergraduate computer science student at San Francisco State University.",
            "In her free time she enjoys walking her three dogs, watching Netflix, and playing video games."
        ]
    },
    "1002": {
        "id": "1002",
        "img": "about/images/team/2JC.jpg",
        "name": "Jeff Cheng",
        "title": "Frontend Lead",
        "intro": ["Jeff is a second-year graduate student in Computer Science at San Francisco State University.",
            "He graduated with a Bachelor of Arts in Economics, with a certified minor in Computer Science, from the University of California, Davis.",
            "He is interested in enhancing user-experience, preferrably for those with special needs.",
            "Jeff enjoys drawing, reading, and hiking in his spare time."
        ]
    },
    "1003": {
        "id": "1003",
        "img": "about/images/team/3AS.jpg",
        "name": "Allen Sun",
        "title": "Backend Lead & Database Master",
        "intro": [
            "Allen Sun is in the second year of the masters program in Computer Science at San Francisco State University.",
            "His skill set includes AI, ML, Python, NumPy, Pandas, AWS, GCP, Tableau, Matplotlib, Seaborn, Scikit-Learn, TensorFlow, PySpark, MySQL, Linux, Django, HTML, CSS, JS, and Apache."
        ]
    },
    "1004": {
        "id": "1004",
        "img": "about/images/team/4PA.jpg",
        "name": "Paul Asu",
        "title": "Github Master",
        "intro": [
            "I am Asu Paul a senior in the Computer Science department at the San Francisco State University.",
            "I love traveling and spending time with my family.",
            "Originally I'm from Nigeria-the most populous black nation, in West Africa."
        ]
    },
    "1005": {
        "id": "1005",
        "img": "about/images/team/5KO.jpg",
        "name": "Kevin Ortiz",
        "title": "Developer",
        "intro": [
            "Kevin Ortiz is a 4th year undergraduate at San Francisco State University.",
            "Kevin's major is Computer Science On the days he is not in class, he walks his two dogs and also goes bike riding.",
            "He also enjoys traveling and if he can live anywhere it will be anywhere that is near the beach!"
        ]
    },

    "1006": {
        "id": "1006",
        "img": "about/images/team/6KW.jpg",
        "name": "Kevin Wei",
        "title": "Developer",
        "intro": [
            "Kevin is a fourth year undergraduate student at San Francisco State University. He is studying Computer Science",
            "He really likes playing Video Games and has a special attachment to Pokemon since childhood. :D"
        ]
    }
}

def about(request):
    content = {
        "title": "About", 
        "team": team,
    }
    return render(request, 'about.html', content)

def profile(request, name, id):
    content = {
        "title": team[id]["name"], 
        "profile": team[id]
    }
    return render(request, 'profile.html', content)

