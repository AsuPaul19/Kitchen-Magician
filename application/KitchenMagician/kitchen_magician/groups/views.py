from django.core.checks.messages import Error
from django.shortcuts import render
from groups.db.group_forum_data_fetch import GroupDataFetch
from groups.models import Group, GroupUser
from groups.models import GroupComment
from groups.db.groups_data_fetch import Groups


def groups(request):
    context = {
        "title": "Groups",
    }
    try:
        user = request.user
        groups = Groups(user)
        context["joined_groups"] = groups.joined_groups
        context["available_groups"] = groups.available_groups

    except Exception as e:
        print(e)
        user = None
        groups = Group.objects.all()
        context["joined_groups"] = None
        context["available_groups"] = groups

    return render(request, 'groups/groups.html', context)
    
def group_forum(request, group_id=None):
    context = {
        "title": "GROUPS_FORUM",
        "group_id": group_id,
        "name": "",
        "img_path": "",
        "users": "",
        "comments": ""
    }

    if request.method == "POST":
        data = request.POST
        group_id = data.get("group_id")
        group = Group.objects.filter(id=group_id).first()
        # update comment
        comment = data.get("comment", False)
        if comment:
            group_comment = GroupComment(group=group, comment=comment, user=request.user)
            group_comment.save()
        
        # POST for Change Member
        join_group = data.get('join_group', False)
        if join_group:
            user = request.user
            if join_group == "join":
                group_user = GroupUser(group=group, user=user)
                group_user.save()
            elif join_group == "leave":
                group_user = GroupUser.objects.filter(group=group, user=user).first()
                group_user.delete()


    # group-info
    group = GroupDataFetch(group_id=group_id)
    if group:
        group_data = group.group_data
        context["name"] = group_data["name"]
        context["img_path"] = group_data["img_path"]
        context["users"] = group_data["users"]
        context["comments"] = group_data["comments"]
    
    # if the user joined the group
    try:
        user = request.user
        group = Group.objects.filter(id=group_id).first()
        context["is_joined"] = GroupUser.objects.filter(group=group, user=user).first()

    except Exception as e:
        print(e)
        context["is_joined"] = False

    return render(request, 'groups/group_forum.html', context)



