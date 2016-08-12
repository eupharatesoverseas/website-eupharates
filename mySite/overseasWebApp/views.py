# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    return render(request,'overseasWebApp/home.html')


def about(request):
    return render(request,'overseasWebApp/about.html')

def it(request):
    return render(request,'overseasWebApp/IT.html')

# Create your views here.
