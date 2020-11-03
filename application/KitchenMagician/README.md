# **Implementation**

-   [Setup(MacOS)](#Setup)


Folder Tree
```bash
-- KitchenMagician
    |-- README.md
    |-- env
    |-- kitchen_magician
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
    |-- requirements.txt
```


1. **Upgrade python**

```shell
sudo apt-get upgrade
sudo apt-get upgrade python
```

2. **Install PIP**

```shell
# python 2
sudo apt-get install python-pip
# python 3
sudo apt-get install python3-pip
```

3. **Setup env**

    1. Install `python3-venv`

    ```shell
    sudo apt-get install python3-venv
    ```

    2. Create env and activate (If this no `env` in the folder, create one; otherwise, skip this step)

        - create env 

            ```shell
            python3 -m venv env
            ```

        - activate env

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
    - Go to the folder `kitchen_magician`

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
    ```

    - Run the application:
    ```shell
    # python2
    python manage.py runserver

    # python3 
    python3 manage.py runserver
    ```

    - If everything works, you see the following output on the command line:

    ```shell
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    November 03, 2020 - 02:20:04
    Django version 3.1.1, using settings 'kitchen_magician.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ```
    - Open the link `http://127.0.0.1:8000/`


-   [Issues](#Issues)