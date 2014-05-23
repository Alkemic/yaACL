#-*- coding:utf-8 -*-
from yaacl.decorators import acl_register_view


@acl_register_view('test_acl.index')
def index(request):
    pass


@acl_register_view('test_acl.other_index', 'This is the "other" index')
def other_index(request):
    pass


@acl_register_view('test_acl.utf_test', u'Zażółć gęślą jaźń')
def utf_test(request):
    pass

