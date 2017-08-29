# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404
from wines.models import Wine
from wines.forms import WineForm

def index(request):
    wines = Wine.objects.all()
    return render(request, 'index.html', {'wines': wines,})

def wine_detail(request, slug):
    wine = Wine.objects.get(slug=slug)
    return render(request, 'wines/wine_detail.html', {'wine': wine,})

@login_required
def edit_wine(request, slug):
    wine = Wine.objects.get(slug=slug)
    if wine.user != request.user:
        raise Http404
    form_class = WineForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=wine)
        if form.is_valid():
            form.save()
            return redirect('wine_detail', slug=wine.slug)
    else:
        form = form_class(instance=wine)
    return render(request, 'wines/edit_wine.html', {'wine': wine,'form': form,})

def create_wine(request):
    form_class = WineForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            wine = form.save(commit=False)
            wine.user = request.user
            wine.slug = slugify(wine.name)
            wine.save()
            return redirect('wine_detail', slug=wine.slug)
    else:
        form = form_class()
    return render(request, 'wines/create_wine.html', {'form': form,})


def browse_by_name(request, initial=None):
    if initial:
        wines = Wine.objects.filter(name__istartswith=initial)
        wines = wines.order_by('name')
    else:
        wines = Wine.objects.all().order_by('name')

    return render(request, 'search/search.html', {'wines': wines, 'initial': initial,})
