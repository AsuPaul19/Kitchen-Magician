# Application Folder

## Purpose
The purpose of this folder is to store all the source code and related files for your team's application. Source code MUST NOT be in any of folder. <strong>YOU HAVE BEEN WARNED</strong>

You are free to organize the contents of the folder as you see fit. But remember your team is graded on how you use Git. This does include the structure of your application. Points will be deducted from poorly structured application folders.

## Please use the rest of the README.md to store important information for your team's application.

# High-level System Architecture and Technologies

| System Architecture and Technologies | Tootls/Version |
|    :--    |     :--     |
| Server Host | Google Compute Engine 2vCPU 4 GB RAM |
| Operating System | Ubuntu 20.04 LTS |
| Database | MySQL 8.0.21 |
| Web Server | Apache 2.4 |
| Server-Side Language | Python3.7+ |
| Front-Side Language | HTML, CSS, JavaScript |
| Supported Browsers | Chrome, Firefox |
| Web Framework | React, Django |
| API Test | Postman |
| IDE | VS Code |
| Web Analytics | GTmetrix |
| SSL Cert | Certbot |



# **Implementation to GCP**

- [Ubuntu](#Ubuntu)
- [MySQL-on-GCP-VM-Engine](#MySQL-on-GCP-VM-Engine)
- [Apache-Server](#Apache-Server)
- [Domain](#Domain)
- [Create-SSL-Certificate](#Create-SSL-Certificate)
- [Issues](#Issues)


## Ubuntu 

Get ubuntu version: 
version -- 20.04.1 LTS (Focal Fossa)

```
cat /etc/os-release
```

1. Upgrade python

  ```
  sudo apt-get upgrade
  sudo apt-get upgrade python
  ```

2. **Install PIP**

  ```
  # python 2
  sudo apt-get install python-pip	    
  # python 3
  sudo apt-get install python3-pip	
  ```

3. **Setup env**


   1. Install `python3-venv`

    ```
    sudo apt-get install python3-venv
    ```

   2. Create env and activate 

      - create env (If `env` not created yet.)

        ```
        python3 -m venv env
        ```

      - activate env

        ```
        source env/bin/activate
        ```

4. **ALL-IN-ONE. Install requirements**

  ```
  pip3 install -r requirements.txt
  ```

  (If step 4 not works, go to 5.)

5. **Install Django**

  ```
  pip3 install Django
  ```

6. **Install mysqlclient**

  - Install **[mysqlclient](https://github.com/PyMySQL/mysqlclient-python)**

    - You may need to install the Python 3 and MySQL development headers and libraries like so:

      ```
      # Debian / Ubuntu
      sudo apt-get install python3-dev default-libmysqlclient-dev build-essential 
      ```

    - Then you can install mysqlclient via pip now:

      ```
      pip3 install mysqlclient
      ```

  **(If obove step doesn't work, skip the step install Homebrew)**

  - Install Homebrew

    [Can I use Homebrew on Ubuntu?](https://stackoverflow.com/questions/33353618/can-i-use-homebrew-on-ubuntu)

    - Installing by cloning:

      ```
      git clone https://github.com/Homebrew/linuxbrew.git ~/.linuxbrew
      ```

    - Add the following to `.bash_profile`:

      ```
      export PATH="$HOME/.linuxbrew/bin:$PATH"
      export MANPATH="$HOME/.linuxbrew/share/man:$MANPATH"
      export INFOPATH="$HOME/.linuxbrew/share/info:$INFOPATH"
      ```




6. **Add External IP**

    Add External IP of VM into `ALLOWED_HOSTS = ['']` in `setting.py`.

7.  **Run Server**

  - On local:

    ```
    python3 manage.py runserver
    ```

  - On Cloud:

    ```
    sudo $(which python) manage.py runserver 0.0.0.0:80
    ```
    
    or enter root and then run it.
    
    ```
    sudo su

    python3 manage.py runserver 0.0.0.0:80
    ```


  - open External ip:

    ```
    http://external-ip-here
    ```


## MySQL-on-GCP-VM-Engine

*Reference*

  - **[Connecting to GCP Compute Engine with MySQL on a Remote Host](https://pieter-duplessis.co.za/blog/connecting-to-gcp-compute-engine-with-mysql-on-a-remote-ost/)**

  - **[Tutorial - Remote access to mysql on google compute engine](https://www.youtube.com/watch?v=8oF4ku_7vxM)**

  - **[MySQL Crash Course | Learn SQL](https://www.youtube.com/watch?v=9ylj9NR0Lcg)**

  - **[MySQL Cheat Sheet](https://gist.github.com/bradtraversy/c831baaad44343cc945e76c2e30927b3)**

  - **[Handy MySQL Commands](http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm)**

1. **Install MySQL on VM Instance**

  ```
  $ sudo apt-get update
  $ sudo apt-get install mysql-server
  ```

2. **Improve MySQL Installation Security(Optional)**

  ```
  $ sudo mysql_secure_installation
  ```

3. **Create a User and their Privileges**

  - Access MySQL with the root user

    No possword needed at this step. Press 'return'.

    ```
    $ sudo mysql -u root -p
    ```

  - Create a Database for test

    ```
    mysql> CREATE DATABASE fridge;
    ```

  - Create the user and password that we will use to connect to MySQL

    ```
    mysql> CREATE USER team1@'%' IDENTIFIED BY 'team1';
    ```

  - If issue pops up: 

    `MySQL ERROR 1819 (HY000): Your password does not satisfy the current policy requirements`

    Troubel Shoot here: **[Fix – MySQL ERROR 1819 (HY000): Your password does not satisfy the current policy requirements](https://ostechnix.com/fix-mysql-error-1819-hy000-your-password-does-not-satisfy-the-current-policy-requirements/)**

      - Show validation policy

      ```
      mysql> SHOW VARIABLES LIKE 'validate_password%';
      ```

      - Change password validation policy

      ```
      mysql> SET GLOBAL validate_password.policy = 0;
      ```

      - or

      ```
      mysql> SET GLOBAL validate_password.policy=LOW;
      ```

  - Grant the privileges for the user just created:

    ```
    mysql> GRANT ALL PRIVILEGES ON fridge.* TO team1@'%';
    ```

  - Flush the privileges (reload the privilege table):

    ```
    mysql> FLUSH PRIVILEGES;
    ```

4. **Setup MySQL Binding Address**

  - Get the file:

    ```
    $ cd /etc/mysql/mysql.conf.d/
    $ nano mysqld.cnf
    ```

  - Find the line with the `bind-address`: 

    ```
    bind-address            = 127.0.0.1
    ```

  - Change the IP address to `0.0.0.0`: 

    ```
    bind-address            = 0.0.0.0
    ```

  - Save and close the file.

5. **Firewall Setup on Google Cloud**

    *Reference*

  - **[Tutorial - Remote access to mysql on google compute engine](https://www.youtube.com/watch?v=8oF4ku_7vxM)** From 5:30.

6. **Test connection to MySQL on the Instance**

- Test port: input External IP and Port(3306)
  - **[yougetsignal](https://www.yougetsignal.com/tools/open-ports/M)** 

  - It might take a whie to see the Port open.

- Directly connect to mysql from other VM.

  ```
  mysql -h 34.123.110.159 -P 3306 -u team1 -p

  team1
  ```

7. **Set up in Djangon**

Chang parameters in `setting.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # database IP（local: localhost or 127.0.0.1）
        'HOST': '34.123.110.159',
        # MySQL port
        'PORT': 3306,
        # database user and password
        'USER': 'team1',
        'PASSWORD': 'team1',
        #Database Name
        'NAME': 'fridge',
        # character 
        'CHARSET': 'utf8',
        # Timezone
        'TIME_ZONE': 'UTC',
    }
}
```


## Apache-Server 

*Reference* 

  - **[What are web servers and how do they work (with examples httpd and nodejs)](https://www.youtube.com/watch?v=JhpUch6lWMw)**

  - **[27 | Host django application using apache and wsgi | by Hardik Patel](https://www.youtube.com/watch?v=s0RX_YU9eJM&t=948s)**

  - **[Using Apache Bench for Simple Load Testing](https://www.petefreitag.com/item/689.cfm)**

1. **Install Apache**

  ```
  sudo apt-get install apache2
  ```

2. **Test Apache**

  ```
  sudo apachectl start
  ```
  
  or use the heigher authority, system control

  ```
  sudo systemctl start apache2.service
  ```

  open External Ip or localhost to see a "It works" or "Ubuntu" page.


3. **Install WSGI**

- Make sure you have wsgi package installed, by running

  ```
  sudo a2enmod wsgi
  ```

- if its not installed, execute below commands to install

  ```
  # Python2
  sudo apt-get install python-pip apache2 libapache2-mod-wsgi  

  # Python3
  sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3 
  ```



4. **Configuration**

- To configure the WSGI pass, we’ll need to edit the default virtual host file:

  ```
  sudo nano /etc/apache2/sites-available/000-default.conf
  ```

- Get user name:

  ```
  $ whoami
  ```

- Get absolute path:

  ```
  $ pwd
  ```

   1. **Static**

    We will use an alias to tell Apache to map any requests starting with /static to the “static” directory within our project folder. Change the DocumentRoot.

    ```
        DocumentRoot /home/allen/csc-648-848-04-jose-fall-2020-01/application/backend

        Alias /static /home/allen/csc-648-848-04-jose-fall-2020-01/application/backend/fridge/magician/static
        <Directory /home/allen/csc-648-848-04-jose-fall-2020-01/application/backend/fridge/magician/static>
            Require all granted
        </Directory>
        
    ```

   2. **wsgi.py**

    Next, we’ll grant access to the wsgi.py file within the second level project directory where the Django code is stored. To do this, we’ll use a directory section with a file section inside. We will grant access to the file inside of this nested construct:

    ```
        <Directory /home/allen/csc-648-848-04-jose-fall-2020-01/application/backend/fridge/fridge>
            <Files wsgi.py>
                Require all granted
            </Files>
        </Directory>
    ```

   3. **WSGIDaemonProcess** 

    Afterwards, we need to specify the process group. This should point to the same name we selected for the WSGIDaemonProcess directive (myproject in our case). Finally, we need to set the script alias so that Apache will pass requests for the root domain to the wsgi.py file:

    ```
        WSGIDaemonProcess fridge python-path=/home/allen/csc-648-848-04-jose-fall-2020-01/application/backend/fridge python-home=/home/allen/csc-648-848-04-jose-fall-2020-01/application/env
        WSGIProcessGroup fridge
        WSGIScriptAlias / /home/allen/csc-648-848-04-jose-fall-2020-01/application/backend/fridge/fridge/wsgi.py
    ```

   4. **ALL IN ONE - Wrapp up i, ii and iii**

    Open conf

    ```
    sudo nano /etc/apache2/sites-available/000-default.conf
    ```

    Edit the file:

    ```
    <VirtualHost *:80>
        . . .

        DocumentRoot /home/allen/csc-648-848-04-jose-fall-2020-01/application/backend

        Alias /static /home/allen/csc-648-848-04-jose-fall-2020-01/application/backend/fridge/magician/static
        <Directory /home/allen/csc-648-848-04-jose-fall-2020-01/application/backend/fridge/magician/static>
            Require all granted
        </Directory>

        <Directory /home/allen/csc-648-848-04-jose-fall-2020-01/application/backend/fridge/fridge>
            <Files wsgi.py>
                Require all granted
            </Files>
        </Directory>
        
        WSGIDaemonProcess fridge python-path=/home/allen/csc-648-848-04-jose-fall-2020-01/application/backend/fridge python-home=/home/allen/csc-648-848-04-jose-fall-2020-01/application/env
        WSGIProcessGroup fridge
        WSGIScriptAlias / /home/allen/csc-648-848-04-jose-fall-2020-01/application/backend/fridge/fridge/wsgi.py

    </VirtualHost>
    ```

4. **Restart Apache**

```
sudo apachctl restart

# or 
sudo serveice apache2 restart
```


## Domain

*Reference*

- **[Free WordPress Hosting On Google Cloud Platform! After 1 year, it costs a few cents a month!](youtube.com/watch?v=cG9kv5-5bPI&list=PLoOI5nqM9nMkx6LK81fcAcO9CUkZN5v52&index=12&t=731s)** From 7:39, step 3.

Domain and server must be under the same account.

## Create-SSL-Certificate

*Reference*

- **[Python Django Tutorial: How to enable HTTPS with a free SSL/TLS Certificate using Let's Encrypt](https://www.youtube.com/watch?v=NhidVhNHfeU&t=146s)**

After certified, use **[SSL Test](https://www.ssllabs.com/)** to test Web.

**Don't forget to keep ufw open**

```
sudo ufw allow https
```


## Issues:
- **Virtual Environment**
  - ERROR

    ```
    Traceback (most recent call last):
      File "manage.py", line 21, in <module>
        main()
      File "manage.py", line 12, in main
        raise ImportError(
    ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
    ```

  - Solution:
    Run env: 

    ```
    source env/bin/activate
    ```

- **Port Permission**

  - ERROR

    ```
    Django version 3.1, using settings 'mid_pipe.settings'
    Starting development server at http://0.0.0.0:80/
    Quit the server with CONTROL-C.
    Error: You don't have permission to access that port.
    ```

  - Solution: Try to call the python binary at your virtualenv explicitly:

    ```
    sudo $(which python) manage.py runserver 0.0.0.0:80
    ```

- **pip3 install mysqlclient**
  
  - ERROR

  ```
  ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
  ```

  - Solution: Install HomeBrew first

    - **[Install Homebrew on Ubuntu 20.04 / 18.04 / Debian 10](https://www.osradar.com/install-homebrew-ubuntu-20-04-debian-10/)**

    - **[Install mysqlclient](https://stackoverflow.com/questions/57643579/how-to-install-mysqlclient-in-python)**

    ```
    brew install mariadb-connector-c

    pip3 install mysqlclient
    ```

- **Apache**
  
  - ERROR

    ```
    Invalid command 'WSGIDaemonProcess', perhaps misspelled or defined by a module not included in the server configuration
    ```

  - Solution: Install wsgi

    **[Invalid command WSGIDaemonProcess Deploy Django application on CentOS 6.7](https://stackoverflow.com/questions/33320889/invalid-command-wsgidaemonprocess-deploy-django-application-on-centos-6-7)**

    make sure you have wsgi package installed, by running

    ```
    sudo a2enmod wsgi
    ```

    if its not installed, execute below commands to install

    ```
    sudo apt-get install python-pip apache2 libapache2-mod-wsgi  # Python2

    sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3 # Python3
    ```

- **user permission**
  - ERROR
    ```
    ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/home/allensun623/env/lib/python3.8/site-packages/numpy-1.19.1.dist-info'
    Consider using the `--user` option or check the permissions.
    ```
  - Solution: don't use `remote shh key` and `GCP SSH` to access the same user and make installation.
