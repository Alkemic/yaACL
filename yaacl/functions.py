#-*- coding:utf-8 -*-
from django.db.models.query_utils import Q
from yaacl.models import ACL

__author__ = 'Daniel Alkemic Czuba <dc@danielczuba.pl>'


def get_acl_resources(user):
    """
    :type user: django.contrib.auth.models.User
    :type name : str

    Checks if user has rights to given resource
    """
    return ACL.objects.filter(Q(user=user)|Q(group__in=user.groups.all())).distinct()


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

    return any([entry.resource.startswith(resource) for entry in get_acl_resources(user)])


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

    return set([entry.id for entry in get_acl_resources(user) if entry.resource.startswith('news.')]) == \
           set([entry.id for name, entry in ACL.acl_list.items() if name.startswith('news.')])
