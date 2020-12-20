from groups.models import Group
from groups.models import GroupUser

# return top n most popular groups
def top_groups(n=4):
    # Fetch all groups
    groups_all = Group.objects.all()
    # Store each group as pair of (group, number of users)
    groups_num = [(group, len(GroupUser.objects.filter(group=group))) for group in groups_all]
    # sort by numbers and get top n groups
    groups_top = sorted(groups_num, key=lambda group: group[1], reverse=True)[:n]
    # return groups object only
    groups_res = [group for group, _ in groups_top]
    return groups_res