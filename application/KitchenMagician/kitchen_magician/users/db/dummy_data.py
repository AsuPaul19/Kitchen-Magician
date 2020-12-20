from django.contrib.auth.models import User
from users.models import Profile
from groups.models import Group
from groups.models import GroupUser
import random

class DummyData():
    def __init__(self, user_num=1):
        self.user_num = user_num
        self.users = self.create_dummy_users()

    def create_dummy_users(self):
        users = []
        for i in range(self.user_num):
            username = f"User{i}" 
            password = username
            email = f"{username}@gmail.com"
            user = User.objects.filter(username=username).first()
            # create user if not exist
            if not user:
                # create a user
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                # create the profile
                default_images_folder = 'default_images/avatars/'
                image_name = f"avatar-flat-{random.randint(1, 50)}.png"
                user_profile = Profile.objects.create(user=user, image=default_images_folder+image_name)
                print(user_profile.image)
                user_profile.save()
            print(f"User - {user}")
            users.append(user)
        return users


    def create_dummy_groupuser(self):
        groups = list(Group.objects.all())
        l_groups = len(groups)
        for user in self.users:
            # random groups sample
            groups_sample = random.sample(groups, l_groups//2)
            for group in groups_sample:
                # If not join the group, add th=o table
                if not GroupUser.objects.filter(user=user, group=group).first():
                    group_user = GroupUser(user=user, group=group)
                    group_user.save()
                    print(f"GroupUser - {group_user}")

