from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import re
import threading


def update_password(username, cur_password, new_password, confirm_password):
    # Send error message if there is any error; else, send an empty error message
    error_msg = ""
    # print(username, cur_password, new_password, confirm_password)
    # user authentication check
    user = authenticate(username=username, password=cur_password)
    # print(user)

    if user:
        # length check
        if len(new_password) < 8:
            error_msg = "Please provide a password with at least 8 characters"

        # password confirmation check
        elif new_password != confirm_password:
            error_msg = "The two new password fields didn’t match."

                # letter check
        elif not regex_password(new_password):
            error_msg = "Please provide a password with at least one digit, one uppercase letter, one lowercase letter, and one special character."

    # If incorrect password
    else:
        error_msg = "Incorrect password"

    # updated successfully if no error
    if not error_msg: 
        # threading to update password
        threading.Thread(user_update_password(username, new_password)).start()

    return error_msg


def regex_password(password):
    """
    Regex
    Password includes at least one digit, one uppercase letter, one lowercase letter, and one special character.
    """
    # The {8,} means "at least 8".
    # print(re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$%^&*?!+-_=])[\w\d@#$]{8,}", password))
    print("regex: ", re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$%^&*?!+-_=])[\w\d@#$]", password))
    return re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$%^&*?!+-_=])[\w\d@#$]", password)
    

def user_update_password(username, password):
    user = User.objects.get(username__exact=username)
    user.set_password(password)
    user.save()