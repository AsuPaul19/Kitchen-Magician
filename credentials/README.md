# Credentials Folder

## The purpose of this folder is to store all credentials needed to log into your server and databases. This is important for many reasons. But the two most important reasons is
    1. Grading , servers and databases will be logged into to check code and functionality of application. Not changes will be unless directed and coordinated with the team.
    2. Help. If a class TA or class CTO needs to help a team with an issue, this folder will help facilitate this giving the TA or CTO all needed info AND instructions for logging into your team's server. 


# Below is a list of items required. Missing items will causes points to be deducted from multiple milestone submissions.

1. Server URL or IP: 34.66.161.176
2. SSH username: allen
3. SSH password or key. files: `team1` and `team1.pub`
    <br> If a ssh key is used please upload the key to the credentials folder.
4. Database URL or IP and port used. 34.123.110.159
    <br><strong> NOTE THIS DOES NOT MEAN YOUR DATABASE NEEDS A PUBLIC FACING PORT.</strong> But knowing the IP and port number will help with SSH tunneling into the database. The default port is more than sufficient for this class.
5. Database username: team1
6. Database password: team1
7. Database name (basically the name that contains all your tables): fridge
8. Instructions on how to use the above information.


- Access to Server:

Enter command:

```
ssh -i <key path> allen@34.66.161.176
```

`<key path>` is the place where you store the downloaded keys `team1` and `team1.pub`, i.g.:

```
ssh -i ~/Desktop/SFSU/ssh/team1 allen@34.66.161.176
```

Input password: `team1`



- Access to MySQL database:

Enter command:

```
mysql -h 34.123.110.159 -P 3306 -u team1 -p
```

Input password: `team1`

# Most important things to Remember
## These values need to kept update to date throughout the semester. <br>
## <strong>Failure to do so will result it points be deducted from milestone submissions.</strong><br>
## You may store the most of the above in this README.md file. DO NOT Store the SSH key or any keys in this README.md file.

**Django admin**

```
user: team1
password: team1
```


