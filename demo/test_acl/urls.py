# -*- coding:utf-8 -*-
from django.conf.urls import *

urlpatterns = patterns(
    'test_acl.views',
    url(r'^$', 'index', name='index'),
    url(r'test/$', 'test', name='test'),
    url(r'other_index/$', 'other_index', name='other_index'),
    url(r'utf_test/$', 'utf_test', name='utf_test'),
)
