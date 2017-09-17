# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import widgets
from django.contrib.auth.models import User
import datetime

def valid_pct(val):
    if val.endswith("%"):
       return float(val[:-1])/100
    else:
       try:
          return float(val)
       except ValueError:          
          raise ValidationError(
              _('%(value)s is not a valid pct'),
                params={'value': value},
           )

YEAR_CHOICES = [(r,r) for r in range(1980, datetime.date.today().year+1)]

class Wine(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	name = models.CharField(max_length=255)
	colour = models.CharField(max_length=50)
	year = models.IntegerField()
	grape = models.CharField(max_length=50)
	region = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	abv = models.CharField(max_length=4, validators=[valid_pct])
	description = models.TextField()
	mode_rating = models.DecimalField(max_digits=3, decimal_places=1)
	winner = models.CharField(max_length=50)
	slug = models.SlugField(unique=True)
    # user = models.OneToOneField(User, blank=True, null=True)