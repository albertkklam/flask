# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.views.generic import TemplateView
from myapp.models import Dreamreal
from myapp.forms import LoginForm
import datetime

class StaticView(TemplateView):
   template_name = "myapp/static.html"

def hello(request):
   today = datetime.datetime.now().date()
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, 'myapp/hello.html', {"today": today})

def randNum(request, num):
   text = "A random number: %s" %num
   return redirect(randFrac, num, "1")
   # return HttpResponse(text)

def randFrac(request, numerator, denominator):
   text = "A random fraction: %s/%s" %(numerator, denominator)
   return HttpResponse(text)

def morning(request):
	return HttpResponse("""<h3>Good morning!</h3>""")

def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = LoginForm()
      
   return render(request, 'myapp/loggedin.html', {"username" : username})