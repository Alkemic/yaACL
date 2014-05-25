#-*- coding:utf-8 -*-
from django.contrib.auth import get_user_model
from django.db.models.signals import class_prepared
from django.conf import settings
from django.db.models import ManyToManyField
from django.utils.translation import ugettext as _

from .models import ACL

# get_user_model()

__author__ = 'Daniel Czuba <dc@danielczuba.pl>'


auth_and_group = (
    getattr(settings, 'AUTH_USER_MODEL', 'auth.User').lower(),
    getattr(settings, 'ACL_GROUP_USER_MODEL', 'auth.group').lower()
)


def add_acl_field(sender, **kwargs):
    """Injection of acl m2m field into current user (auth) and group models, on `class_prepared` signal"""

    if sender._meta.__str__().lower() in auth_and_group:
        field = ManyToManyField(ACL, verbose_name=_('ACL'), blank=True, null=True)
        field.contribute_to_class(sender, 'acl')

class_prepared.connect(add_acl_field)
