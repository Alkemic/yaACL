# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from yaacl.models import ACL

__author__ = 'Daniel Alkemic Czuba <dc@danielczuba.pl>'


class Command(BaseCommand):
    help = _('Imports all defined sql views')

    def handle(self, *args, **options):
        for app in settings.INSTALLED_APPS:
            try:
                __ = __import__("%s.views" % app)
            except ImportError:
                pass

        for view_name, acl in ACL.acl_list.items():
            entry, created = ACL.objects.get_or_create(resource=view_name)

            if created:
                entry.display = acl.display
                entry.save()
