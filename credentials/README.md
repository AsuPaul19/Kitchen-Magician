# Credentials Folder

## The purpose of this folder is to store all credentials needed to log into your server and databases. This is important for many reasons. But the two most important reasons is
    1. Grading , servers and databases will be logged into to check code and functionality of application. Not changes will be unless directed and coordinated with the team.
    2. Help. If a class TA or class CTO needs to help a team with an issue, this folder will help facilitate this giving the TA or CTO all needed info AND instructions for logging into your team's server. 


# Below is a list of items required. Missing items will causes points to be deducted from multiple milestone submissions.

1. Server URL or IP: 34.66.161.176
2. SSH username: allen
3. SSH password or key.
    <br> If a ssh key is used please upload the key to the credentials folder.
4. Database URL or IP and port used. 34.123.110.159
    <br><strong> NOTE THIS DOES NOT MEAN YOUR DATABASE NEEDS A PUBLIC FACING PORT.</strong> But knowing the IP and port number will help with SSH tunneling into the database. The default port is more than sufficient for this class.
5. Database username: team1
6. Database password: team1
7. Database name (basically the name that contains all your tables): frigerator
8. Instructions on how to use the above information.

- Access MySQL database:

enter command:

```
mysql -h 34.123.110.159 -P 3306 -u team1 -p
```

input password: `team1`

# Most important things to Remember
## These values need to kept update to date throughout the semester. <br>
## <strong>Failure to do so will result it points be deducted from milestone submissions.</strong><br>
## You may store the most of the above in this README.md file. DO NOT Store the SSH key or any keys in this README.md file.



# MySQL-on-GCP-CM-Engine

*Reference*

  - **[Connecting to GCP Compute Engine with MySQL on a Remote Host](https://pieter-duplessis.co.za/blog/connecting-to-gcp-compute-engine-with-mysql-on-a-remote-ost/)**

  - **[Tutorial - Remote access to mysql on google compute engine](https://www.youtube.com/watch?v=8oF4ku_7vxM)**


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
    mysql> CREATE DATABASE frigerator;
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
    mysql> GRANT ALL PRIVILEGES ON frigerator.* TO team1@'%';
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
        'NAME': 'frigerator',
        # character 
        'CHARSET': 'utf8',
        # Timezone
        'TIME_ZONE': 'UTC',
    }
}
```

