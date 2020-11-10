from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # CASCADE, once the user is deleted, the profile will be deleted automatically 
    profile_image_folder = 'profile_pics/'
    default_images_folder = 'default_images/'
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    image = models.ImageField(default= default_images_folder + 'default_profile_avatar.jpg', upload_to= profile_image_folder)

    def __str__(self):
        return f'{self.user.username} Profile'