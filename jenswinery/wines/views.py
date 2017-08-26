# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from wines.models import Wine

def index(request):
    wines = Wine.objects.all()
    return render(request, 'index.html', {'wines': wines,})