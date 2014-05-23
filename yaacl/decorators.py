#-*- coding:utf-8 -*-
from functools import wraps
from django.utils.decorators import available_attrs
from yaacl.functions import has_access
from .views import no_access
from .models import ACL


def acl_register_view(view_name, display_name=None):
    """
    :type view_name: str
    :type display_name: unicode
    """
    entry, created = ACL.objects.get_or_create(view=view_name)

    if created or display_name != entry.display:
        entry.display = display_name
        entry.save()

    if not view_name in ACL.acl_list:
        ACL.acl_list[view_name] = entry
    print ACL.acl_list

    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def wrapped_view(request, *args, **kwargs):
            """
            :type request: django.http.request.HttpRequest
            """
            if has_access(request.user, view_name):
                return view_func(request, *args, **kwargs)
            else:
                return no_access(request)

        return wrapped_view

    return decorator
