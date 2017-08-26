# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    number = 6
    thing = "Thing name"
    return render(request, 'index.html', {'number': number, 'thing': thing})