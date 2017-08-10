from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^hello', views.hello, name = 'hello'),
	url(r'^morning/', views.morning, name = 'morning'),
	url(r'^number/(\d+)/', views.randNum, name = 'number'),
	url(r'^fraction/(\d{1,4})/(\d{1,4})', views.randFrac, name = 'fraction'),
	url(r'^static/$', views.StaticView.as_view()),
]