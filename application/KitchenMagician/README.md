# **Implementation**
-   [Tutorial](#Tutorial)
-   [Setup (MacOS)](#Setup(MacOS&Ubuntu))
-   [Issues](#Issues)

## Tutorial

**Django**
- [Python Django Tutorial: Full-Featured Web App Part 1 - Getting Started](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- [Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes](https://www.youtube.com/watch?v=a48xeeo5Vnk&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=2)
- [Python Django Tutorial: Full-Featured Web App Part 3 - Templates](https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3)
- [Python Django Tutorial: Full-Featured Web App Part 5 - Database and Migrations](https://www.youtube.com/watch?v=aHC3uTkT9r8&list=PLoOI5nqM9nMkx6LK81fcAcO9CUkZN5v52&index=13&t=1932s)

**Python**
- [Python Tutorial: VENV (Mac & Linux) - How to Use Virtual Environments with the Built-In venv Module](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)




## Setup (MacOS)



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
        - try 

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