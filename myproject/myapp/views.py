# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime

def hello(request):
   today = datetime.datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "myapp/hello.html", {"today" : today, "days_of_week" : daysOfWeek})

def randNum(request, num):
   text = "A random number: %s"%num
   return HttpResponse(text)

def viewArticles(request, year, month):
   text = "Displaying articles of: %s/%s"%(year, month)
   return HttpResponse(text)

def morning(request):
	return HttpResponse("""<h3>Good morning!</h3>""")
