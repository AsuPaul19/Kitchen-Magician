from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class GroupType(models.Model):
    type = models.CharField(max_length=50)

    class Meta():
        db_table = 'group_type'

    def __str__(self):
        return self.type

class Group(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    group_name = models.CharField(max_length=50)
    group_type = models.ForeignKey(GroupType, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)

    class Meta():
        db_table = 'group'

    def __str__(self):
        return self.group_name

class GroupUser(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta():
        db_table = 'group_user'

    def __str__(self):
        return f'{self.group.group_name} - {self.user.username}'

class GroupComment(models.Model):
    # CASCADE, once the user is deleted, this item will be deleted automatically
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    created = models.DateTimeField(default=timezone.now)

    class Meta():
        db_table = 'group_comment'

    def __str__(self):
        return f'Group - {self.group.group_name}, User - {self.user.username}, Comment - {self.comment}'