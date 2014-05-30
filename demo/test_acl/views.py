#-*- coding:utf-8 -*-
from django.template import loader
from django.template.response import TemplateResponse

from yaacl.decorators import acl_register_view


def index(request):
    template = loader.get_template('test_acl/index.html')

    return TemplateResponse(request, template)


@acl_register_view('test_acl.test')
def test(request):
    pass


@acl_register_view('test_acl.other_index', 'This is the "other" index')
def other_index(request):
    pass


@acl_register_view('test_acl.utf_test', u"Zażółć gęślą jaźń")
def utf_test(request):
    pass

