#-*- coding:utf-8 -*-
from django.db.models.signals import class_prepared
from django.conf import settings
from django.db.models import ManyToManyField
from django.utils.translation import gettext_lazy as _

from .models import ACL

__author__ = 'Daniel Czuba <dc@danielczuba.pl>'


auth_and_group = {
    getattr(settings, 'AUTH_USER_MODEL', 'auth.User').lower(): 'user',
    getattr(settings, 'ACL_GROUP_USER_MODEL', 'auth.group').lower(): 'group'
}


def add_acl_field(sender, **kwargs):
    """Injection of acl m2m field into current user (auth) and group models, on `class_prepared` signal"""

    if sender._meta.__str__().lower() in auth_and_group:
        field = ManyToManyField(ACL, verbose_name=_('ACL'), blank=True, null=True, related_name=auth_and_group[sender._meta.__str__().lower()])
        field.contribute_to_class(sender, 'acl')

class_prepared.connect(add_acl_field)
