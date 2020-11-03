# Credentials Folder

## The purpose of this folder is to store all credentials needed to log into your server and databases. This is important for many reasons. But the two most important reasons is
    1. Grading , servers and databases will be logged into to check code and functionality of application. Not changes will be unless directed and coordinated with the team.
    2. Help. If a class TA or class CTO needs to help a team with an issue, this folder will help facilitate this giving the TA or CTO all needed info AND instructions for logging into your team's server. 


# Below is a list of items required. Missing items will causes points to be deducted from multiple milestone submissions.

1. Server URL or IP: 34.66.161.176
2. SSH username: allen
3. SSH password or key. files: `kitchen_magician` and `kitchen_magician.pub`
    <br> If a ssh key is used please upload the key to the credentials folder.
4. Database URL or IP and port used. 34.123.110.159
    <br><strong> NOTE THIS DOES NOT MEAN YOUR DATABASE NEEDS A PUBLIC FACING PORT.</strong> But knowing the IP and port number will help with SSH tunneling into the database. The default port is more than sufficient for this class.
5. Database username: kitchen_magician
6. Database password: kitchen_magician
7. Database name (basically the name that contains all your tables): kitchen_magician
8. Instructions on how to use the above information.


- Access to Server:

Enter command:

```
ssh -i <key path> allen@34.66.161.176
```

`<key path>` is the place where you store the downloaded keys `kitchen_magician` and `kitchen_magician.pub`, i.g.:

```
ssh -i ~/Desktop/SFSU/ssh/kitchen_magician kitchen_magician@34.66.161.176
```

Input password: `kitchen_magician`



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

## Django Admin

**Application Administration**: https://www.allensun623.com/admin

```
user: team1
password: team1
```



## Issues

- **UNPROTECTED PRIVATE KEY FILE!**
  - ERROR

  ```
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  Permissions 0555 for '/Users/allen/Desktop/kitchen_magician.pub' are too open.
  It is required that your private key files are NOT accessible by others.
  This private key will be ignored.
  Load key "/Users/allen/Desktop/kitchen_magician.pub": bad permissions
  ```

  - Solution

  What happened is the key you're trying to use (key.pem in the example above) is too accessible to users on the system.

  This is a bad thing because then you're not the only one able to use the key, which defeats the purpose. Private keys should only be accessible to one user.

  For example, if an attacker somehow gains access to any of the accounts on your system, then they'd be able access the key, as opposed to having to get access to your account specifically. This gives them too many opportunities to get to the private key.

  ```
  sudo ssh -i ~/Desktop/SFSU/ssh/kitchen_magician kitchen_magician@34.66.161.176
  ```

