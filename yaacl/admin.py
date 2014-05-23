#-*- coding:utf-8 -*-
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext as _

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

admin.site.register(User, ACLUserAdmin)
admin.site.register(ACL)