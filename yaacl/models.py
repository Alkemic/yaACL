# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class ACL(models.Model):
    acl_list = {}
    resource = models.CharField(_("Resource name"), max_length=255, db_index=True)
    display = models.CharField(_("displayed name"), max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(_("Creation time"), default=datetime.now())
    is_available = models.BooleanField(_("Is available to assign"), default=True)

    class Meta:
        app_label = 'yaacl'

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u"%s (%s)" % (self.display, self.resource) if self.display else u"%s" % self.resource
