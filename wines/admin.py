# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from wines.models import Wine

class WineAdmin(admin.ModelAdmin):
    model = Wine
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Wine, WineAdmin)