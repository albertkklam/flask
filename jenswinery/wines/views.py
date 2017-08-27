# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from wines.models import Wine
from wines.forms import WineForm

def index(request):
    wines = Wine.objects.all()
    return render(request, 'index.html', {'wines': wines,})

def wine_detail(request, slug):
    wine = Wine.objects.get(slug=slug)
    return render(request, 'wines/wine_detail.html', {'wine': wine,})

def edit_wine(request, slug):
    wine = Wine.objects.get(slug=slug)
    form_class = WineForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=wine)
        if form.is_valid():
            form.save()
            return redirect('wine_detail', slug=wine.slug)
    else:
        form = form_class(instance=wine)
    return render(request, 'wines/edit_wine.html', {'wine': wine,'form': form,})