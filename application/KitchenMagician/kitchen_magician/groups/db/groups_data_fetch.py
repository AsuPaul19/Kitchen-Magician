from groups.models import Group
from groups.models import GroupUser


class Groups():
    def __init__(self, user=None):
        self.user = user
        self.joined_groups = self.get_joined_groups(user)
        self.available_groups = self.get_available_groups()

    def get_joined_groups(self, user):
        groups = None
        if user:
            joined_groups = GroupUser.objects.filter(user=user)
            groups = [joined_group.group for joined_group in joined_groups]
        return groups

    def get_available_groups(self):
        groups = Group.objects.all()
        # If a group is not a joined group, add to available_groups
        available_groups = [group for group in groups if group not in self.joined_groups]
        return available_groups