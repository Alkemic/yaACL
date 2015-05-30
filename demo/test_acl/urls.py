# -*- coding:utf-8 -*-
from django.conf.urls import *

from .views import Index, TestClassBasedView

urlpatterns = patterns(
    'test_acl.views',
    url(r'^$', Index.as_view(), name='index'),
    url(r'^$', TestClassBasedView.as_view(), name='index'),
    url(r'test/$', 'test', name='test'),
    url(r'other_index/$', 'other_index', name='other_index'),
    url(r'utf_test/$', 'utf_test', name='utf_test'),
)
