from django.contrib import admin
from .models import Group
from .models import GroupComment
from .models import GroupType
from .models import GroupUser


admin.site.register(Group)
admin.site.register(GroupComment)
admin.site.register(GroupType)
admin.site.register(GroupUser)