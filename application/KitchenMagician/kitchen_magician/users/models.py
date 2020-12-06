from django.db import models
from django.contrib.auth.models import User
import random

# Create your models here.
class Profile(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically 
    profile_image_folder = 'profile_pics/'
    default_images_folder = 'default_images/avatars/'
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    image_name = f"avatar-flat-{random.randint(1, 50)}.png"
    image = models.ImageField(default= default_images_folder + image_name, upload_to= profile_image_folder)

    class Meta():
        db_table = 'user_profile'

    def __str__(self):
        return f'{self.user.username} Profile'