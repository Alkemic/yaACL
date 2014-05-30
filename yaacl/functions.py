#-*- coding:utf-8 -*-
from yaacl.models import ACL

__author__ = 'Daniel Alkemic Czuba <dc@danielczuba.pl>'


def has_access(user, resource):
    """
    :type user: django.contrib.auth.models.User
    :type name : str

    Checks if user has rights to given resource
    """
    if not user or not user.is_authenticated():
        return False

    if user.is_superuser:
        return True

    return any([entry.resource.startswith(resource) for entry in user.acl.all()])


def has_all_access(user, resource):
    """
    :type user: django.contrib.auth.models.User
    :type name : str

    Checks if user has rights to given resource
    """
    if not user or not user.is_authenticated():
        return False

    if user.is_superuser:
        return True

    return set([entry.id for entry in user.acl.all() if entry.resource.startswith('news.')]) == \
           set([entry.id for name, entry in ACL.acl_list.items() if name.startswith('news.')])
