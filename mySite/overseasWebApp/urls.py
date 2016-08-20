# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from . import views

urlpatterns = [

url(r'^$',views.index, name='index'),
url(r'^about/$',views.about, name='about'),
url(r'^it/$',views.it, name='information'),
url(r'^import/$',views.import_page, name='import'),
url(r'^contact/$',views.contact_page, name='contact'),
]
