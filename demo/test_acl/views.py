# -*- coding:utf-8 -*-
from django.views.generic import View, TemplateView

from yaacl.decorators import acl_register_view, acl_register_class


class Index(TemplateView):
    template_name = 'test_acl/index.html'


@acl_register_view()
def test(request):
    pass


@acl_register_view('This is the "other" index')
def other_index(request):
    pass


@acl_register_view(u"Zażółć gęślą jaźń")
def utf_test(request):
    pass


@acl_register_view(u"Another test")
def another_test(request):
    pass


@acl_register_class(u"Class based view")
class TestClassBasedView(View):
    pass
