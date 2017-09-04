# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
# 	username = models.CharField(max_length=30)

# 	def __str__(self):
# 		return self.username

class Wine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    # user = models.OneToOneField(User, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
		return self.name
