from django.contrib.auth.models import User
from groups.models import Group
from groups.models import GroupUser
from groups.models import GroupComment

class GroupDataFetch():
    def __init__(self, group=None, group_id=None):
        self.group = group
        self.group_id = group_id
        self.group_data = self.get_data()

    def get_data(self):
        group = Group.objects.filter(id=self.group_id).first()
        group_data = {
            "group_id": self.group_id,
            "name": "",
            "img_path": "",
            "users": "",
            "comments": ""
        }
        if group:
            group_data["name"] = group.name
            group_data["img_path"] = group.img_path
            group_data["users"] = self.get_users(group)
            group_data["comments"] = self.get_comments(group)

        return group_data

    def get_users(self, group):
        users = []
        group_users = GroupUser.objects.filter(group=group)
        for group_user in group_users:
            user_data = {
                "username": group_user.user.username,
                "image": group_user.user.profile.image,
            }
            users.append(user_data)
        return users

    def get_comments(self, group):
        comments_data = []
        all_comments = GroupComment.objects.filter(group=group)
        if all_comments:
            for comment in all_comments:
                comments_data.append(
                    {
                        'user': comment.user.username,
                        'user_avatar': comment.user.profile.image,
                        'comment': comment.comment,
                        'created': comment.created
                    }
                )

        return comments_data

