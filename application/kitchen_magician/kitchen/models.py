

from django.db import models
from django.utils import timezone
# 1 to many relationship
from django.contrib.auth.models import User

class Recipe(models.Model):
  title = models.CharField(max_length=100)
  # if a user is deleted, we will the post, but the reverse doesn't hold:  one-way street
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(default=timezone.now)
  content = models.TextField()

  # to make the output more descriptive in the shell
  def __str__(self):
    return self.title