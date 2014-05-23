#-*- coding:utf-8 -*-
__author__ = 'Daniel Alkemic Czuba <dc@danielczuba.pl>'


def has_access(user, resource):
    """
    :type user: django.contrib.auth.models.User
    :type name : str

    Checks if user has rights to given resource
    """
    if user.is_superuser:
        return True

    return any([entry.resource.startswith(resource) for entry in user.acl.all()])
