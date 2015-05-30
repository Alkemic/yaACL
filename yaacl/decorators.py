# -*- coding:utf-8 -*-
from functools import wraps

from django.utils.decorators import method_decorator, available_attrs
from yaacl.functions import has_access

from .views import no_access
from .models import ACL


def acl_register_view(display_name=None, resource_name=None):
    """
    :type display_name: unicode
    :type resource_name: str
    """

    def decorator(view_func, display_name, resource_name):
        if resource_name is None:
            resource_name = "%s.%s" % (
                view_func.__module__,
                view_func.__name__,
            )

        if resource_name not in ACL.acl_list:
            ACL.acl_list[resource_name] = display_name

        @wraps(view_func, assigned=available_attrs(view_func))
        def wrapped_view(request, *args, **kwargs):
            """
            :type request: django.http.request.HttpRequest
            """
            has_access_to_resource = (
                request.user.is_authenticated() and
                has_access(request.user, resource_name)
            )
            if has_access_to_resource:
                return view_func(request, *args, **kwargs)
            else:
                return no_access(request)

        return wrapped_view

    return lambda view_func: decorator(view_func, display_name, resource_name)


def acl_register_class(display_name=None, resource_name=None):
    def klass_decorator(klass, display_name, resource_name):
        if resource_name is None:
            resource_name = "%s.%s" % (klass.__module__, klass.__name__)

        klass.dispatch = method_decorator(
            acl_register_view(display_name, resource_name)
        )(klass.dispatch)

        return klass

    return lambda klass: klass_decorator(klass, display_name, resource_name)
