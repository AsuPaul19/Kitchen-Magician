# **Implementation**
-   [Tutorial](#Tutorial)
-   [Setup-MacOS_Ubuntu](#Setup-MacOS_Ubuntu)
-   [Issues](#Issues)
-   [Github-Cheat-Sheet](#Github-Cheat-Sheet)

## Tutorial

**Django**
- [Python Django Tutorial: Full-Featured Web App Part 1 - Getting Started](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- [Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes](https://www.youtube.com/watch?v=a48xeeo5Vnk&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=2)
- [Python Django Tutorial: Full-Featured Web App Part 3 - Templates](https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3)
- [Python Django Tutorial: Full-Featured Web App Part 5 - Database and Migrations](https://www.youtube.com/watch?v=aHC3uTkT9r8&list=PLoOI5nqM9nMkx6LK81fcAcO9CUkZN5v52&index=13&t=1932s)

**Python**
- [Python Tutorial: VENV (Mac & Linux) - How to Use Virtual Environments with the Built-In venv Module](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)




## Setup-MacOS_Ubuntu



Folder Tree
```bash
-- KitchenMagician
    |-- README.md
    |-- env
    |-- kitchen_magician
    |   |-- about
    |   |-- home 
    |   |-- media
    |   |-- users
    |   |-- db.sqlite3       
    |   |-- kitchen_magician 
    |   |-- recipe
    |   |-- groups           
    |   |-- manage.py        
    |   |-- search
    |   |-- testing
    |-- requirements.txt
```


1. **Upgrade python**

```shell
sudo apt-get upgrade
sudo apt-get upgrade python
```

2. **Install PIP**


-  Ubuntu

    ```shell
    # python 2
    sudo apt-get install python-pip
    # python 3
    sudo apt-get install python3-pip
    ```

- Mac
    ```shell
    sudo easy_install pip
    ```




3. **Setup env**

    1. Install `python3-venv` for Ubuntu only.
    - Ubuntu
        ```shell
        sudo apt-get install python3-venv
        ```

    2. Create virtual environment `env` and activate (If this no `env` in the folder, create one; otherwise, skip this step)

        - create env 

            ```shell
            python3 -m venv env
            ```

            - Window
            ```shell
            py -m venv env
            ```

        - activate `env`

            ```shell
            source env/bin/activate
            ```

            or

            ```shell
            . env/bin/activate
            ```

4. **ALL-IN-ONE. Install requirements**
Install required python packages for this application

```shell
pip3 install -r requirements.txt
```
All required packages
```
asgiref==3.2.10
Django==3.1.1
django-crispy-forms==1.9.2
mysqlclient==2.0.1
Pillow==8.0.1
pytz==2020.1
sqlparse==0.4.1
```


5. **Run the development server**
    1. Go to the folder `kitchen_magician`

    ```bash
    -- kitchen_magician
        |-- about
        |-- home 
        |-- media
        |-- users
        |-- db.sqlite3       
        |-- kitchen_magician 
        |-- recipe
        |-- groups           
        |-- manage.py        
        |-- search
        |-- testing

    ```

    2. Run the application:
    ```shell
    # python2
    python manage.py runserver

    # python3 
    python3 manage.py runserver
    ```

    3. If everything works, you see the following output on the command line:

    ``` 
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    November 03, 2020 - 02:20:04
    Django version 3.1.1, using settings 'kitchen_magician.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ```
    - Open the link `http://127.0.0.1:8000/`



## Issues:

-   **Virtual Environment**

    -   ERROR

        ```
        Traceback (most recent call last):
          File "manage.py", line 21, in <module>
            main()
          File "manage.py", line 12, in main
            raise ImportError(
        ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
        ```

    -   Solution:
        Run env:

        ```
        source env/bin/activate
        ```

-   **Port Permission**

    -   ERROR

        ```
        Django version 3.1, using settings 'mid_pipe.settings'
        Starting development server at http://0.0.0.0:80/
        Quit the server with CONTROL-C.
        Error: You don't have permission to access that port.
        ```

    -   Solution: Try to call the python binary at your virtualenv explicitly:

        - Local

        ```
        # python
        python manage.py runserver

        # python 3
        python3 manage.py runserver
        ```


        - Cloud
        ```
        sudo $(which python) manage.py runserver 0.0.0.0:80
        ```

-   **Consider using the `--user` option or check the permissions.**    
    - ERROR
        ```
        ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: 'c:\\python38\\Scripts\\django-admin.py'
        Consider using the `--user` option or check the permissions.
        ```

    - Solution: 
        - View all packages you have installed in the environment.
        ```
        # python
        pip

        # python3
        pip3 list
        ```

        - Compare with the list of required packaged. Install missed package individually. 
        ```
        # python
        python -m pip install package-name

        # python3 
        python3 -m pip install package-name
        ```

        - windows 
        ```
        py -m pip install package-name
        ```

        **All required packages**
        ```
        asgiref==3.2.10
        Django==3.1.1
        django-crispy-forms==1.9.2
        mysqlclient==2.0.1
        Pillow==8.0.1
        pytz==2020.1
        sqlparse==0.4.1
        ```


## Github-Cheat-Sheet
*Reference*
- **[github-git-cheat-sheet](https://training.github.com/downloads/github-git-cheat-sheet/)**
### Branches
- **[git-cheat-sheet-education](https://education.github.com/git-cheat-sheet-education.pdf)**
Branches are an important part of working with Git. Any commits you make will be made on the branch you’re currently “checked out” to. Use git status to see which branch that is.

- Creates a new branch

```shell
git branch [branch-name]
```

- Switches to the specified branch and updates the working directory
```shell
git checkout [branch-name]
```

- Creates a new branch based on current working branch and switches to it
```shell
git checkout -b [branch-name]
```

- Combines the specified branch’s history into the current branch. This is usually done in pull requests, but is an important Git operation.
```shell
merge [branch]
```

- Deletes the specified branch
```shell
git branch -d [branch-name]
```

### Synchronize changes
Synchronize your local repository with the remote repository on GitHub.com

- Downloads all history from the remote tracking branches
```shell
git fetch
```

- Combines remote tracking branches into current local branch
```shell
git merge
```

- Uploads all local branch commits to GitHub
```shell
git push
```

- Upload a new branch to Github
```shell
git push --set-upstream origin [branch-name]
```

- Updates your current local working branch with all new commits from the corresponding remote branch on GitHub. git pull is a combination of git fetch and git merge
```shell
git pull
```


### Make changes
Browse and inspect the evolution of project files

- Lists version history for the current branch
```shell
git log
```

- Lists version history for a file, including renames
```shell
git log --follow [file]
```

- Shows content differences between two branches
```shell
git diff [first-branch]...[second-branch]
```

- Outputs metadata and content changes of the specified commit
```shell
git show [commit]
```

- Snapshots the file in preparation for versioning
```shell
git add [file]
```

- Records file snapshots permanently in version history
```shell
git commit -m "[descriptive message]"
```
- Amend the commit 
```shell
git commit --amend
```

### REWRITE HISTORY
Rewriting branches, updating commits and clearing history
- apply any commits of current branch ahead of specified one
```shell
git rebase [branch]
```
- clear staging area, rewrite working tree from specified commit
```shell
git reset --hard [commit]
```





# **Database Instruction**
There is a python file `recipe/recipe_data_fetch.py` for fetching all data for a recipe.

Recipe Info: return a recipe data as a dictionary {key, value}
```python
    recipe_data_json = {
            'user': self.recipe_user(recipe),
            'name': self.recipe_name(recipe),
            'information': self.recipe_information(recipe),
            'ingredients': self.recipe_ingredients(recipe),
            'instructions': self.recipe_instruction(recipe),
            "images": self.recipe_image(recipe),
            "video_link": self.recipe_video_link(recipe),
            "quantity_serve": self.recipe_quantity_serve(recipe),
            "preparation_time": self.recipe_preparation_time(recipe), 
            "courses": self.recipe_courses(recipe),
            "occasions": self.recipe_occasions(recipe),
            "diets": self.recipe_diets(recipe),
        }
```

Instruction of using the class `RecipeDataFetch` in `recipe/recipe_data_fetch.py`

1. fetching recipe data with instance recipe or id recipe_id
    - fetching recipe data with `instance recipe`
    ```python
        from recipe.recipe_data_fetch import RecipeDataFetch
        # Either fetching data with instance recipe
        recipe_instance = RecipeDataFetch(recipe=recipe)
        recipe_data = None
        if recipe_instance.is_valid: # if recipe_instance is valid
            recipe_data = recipe_instance.recipe_data
    ```
    - fetching recipe data with `id recipe_id`
    ```python
        from recipe.recipe_data_fetch import RecipeDataFetch
        # Or fetching data with id recipe_id
        recipe_instance = RecipeDataFetch(recipe_id=recipe_id)
        recipe_data = None
        if recipe_instance.is_valid(): # if recipe_instance is not valid
            recipe_data = recipe_instance.recipe_data
    ```
2. How do we get certain data?

    If the instance recipe or recipe_id is valid, we will get the `recipe_data` as a dictionary.
    | Key                   | Value(Description)    | Type                  |Get value in Python   | Get value in HTML|
    | :-------------------- | :-------------------- | :-------------------- |:-------------------- |:-------------------- |
    | user                  | user name             | String                | recipe_data['user'] | recipe_data.user |
    | name | recipe name | String | recipe_data['name'] | recipe_data.name |
    | information | recipe information | String | recipe_data['information'] | recipe_data.information |
    | ingredients | recipe ingredients | List | recipe_data['ingredients'] | recipe_data.ingredients |
    | instructions | recipe instruction | String | recipe_data['instruction'] | recipe_data.instruction |
    | images | recipe image path | String path for Python; Image file for HTML | recipe_data['image'] | recipe_data.image.url |
    | video_link | recipe video link | String | recipe_data['video_link'] | recipe_data.video_link |
    | quantity_serve | recipe quantity serve | Int | recipe_data['quantity_serve'] | recipe_data.quantity_serve |
    | preparation_time | recipe preparation time | String | recipe_data['preparation_time'] | recipe_data.preparation_time |
    | courses | recipe courses | List | recipe_data['courses'] | recipe_data.courses |
    | occasions | recipe occasions | List | recipe_data['occasions'] | recipe_data.occasions |
    | diets | recipe diets | List | recipe_data['diets'] | recipe_data.diets |

    - **Key**: the key of a dictionary pair
    - **Value(Description)**: the value of a dictionary pair, and its description
    - **String**: Type of value in database
    - **Get value in Python**: The way to use it and get value in Python
    - **Get value in HTML**: The way to use it and get value in HTML

    - e.g. get recipe title in python
    ```python
    if recipe_data: # if recipe_data is not None
       title = recipe_data['name']
    ```
    - e.g. get recipe title in html
        - If we pass recipe data in views, it could write a method. e.g.
        ```python
        def recipe_view(request, recipe=None, recipe_id=None):
            context = {
                    'title': 'RECIPES',
                    'recipe': None,
                }
            recipe_instance = RecipeDataFetch(recipe=recipe, recipe_id=recipe_id)
            # if we fetch the data successfully, send to clients
            if recipe_instance.is_valid:  
                context['recipe'] = recipe_instance.recipe_date
                return render(request, 'recipe.html', context)
            else: #return 404 Page if the recipe doesn't match in the database
                return not_found(request) 

        def not_found(request):
            context = {
                'title': '404 NOT FOUND'
            }
            return render(request, '404.html', context)
        ```
        - In the corresponding `recipe.html` file, get the values. e.g.
        ``` html
        <div id="recipe">
            {% if recipe %}
                <p>User: {{ recipe.user }} </p>
                <p>Title: {{ recipe.name }}</p>
                <p>Information: {{ recipe.information }}</p>
                <p>Ingredient: {{ recipe.ingredients }}</p>
                <p>Instruction: </p>
                {% for instruction in recipe.instructions %}
                <h4>   - Step {{ forloop.counter }}</h4>
                <p>    {{instruction}}</p>
                {% endfor %}
                <p>Image: </p>
                {% if recipe.images %}
                    <img src="{{ recipe.images.url }}" alt="">
                {% endif %}
                <p>Video Link: {{ recipe.video_link }}</p>
                <p>Preparation Time: {{ recipe.preparation_time }}</p>
                <p>Quantity Serve: {{ recipe.quantity_serve }}</p>
                <p>Course: {{ recipe.courses }}</p>
                <p>Occasion: {{ recipe.occasions }}</p>
                <p>Diet: {{ recipe.diets }}</p>
            {% else %}  
                <p>Sorry, we can't find the recipe.</p>
            {% endif %}
        </div>
        ```

