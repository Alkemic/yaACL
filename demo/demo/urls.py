# -*- coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns =[
    url(r'^', include('test_acl.urls', namespace='test-acl')),
    url(r'^admin/', include(admin.site.urls)),
]
