#-*- coding:utf-8 -*-
from django.db.models import get_model
from django.conf import settings
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from .models import ACL

User = get_user_model()

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass


class ACLUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (_('ACL'), {'fields': ('acl',)}),
    )

    filter_horizontal = UserAdmin.filter_horizontal + ('acl',)

if getattr(settings, 'ACL_GROUP_USER_MODEL', 'auth.Group') == 'auth.Group':
    try:
        admin.site.unregister(Group)
    except admin.sites.NotRegistered:
        pass

    app_label, class_name  = getattr(settings, 'ACL_GROUP_USER_MODEL', 'auth.Group').split('.')
    group_model = get_model(app_label, class_name)


    class ACLGroupAdmin(GroupAdmin):
        filter_horizontal = GroupAdmin.filter_horizontal + ('acl',)

    admin.site.register(Group, ACLGroupAdmin)

admin.site.register(User, ACLUserAdmin)
admin.site.register(ACL)