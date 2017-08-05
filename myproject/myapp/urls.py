from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^hello', views.hello, name = 'hello'),
	url(r'^morning/', views.morning, name = 'morning'),
	url(r'^random/(\d+)/', views.randNum, name = 'random'),
	url(r'^articles/(\d{2})/(\d{4})', views.viewArticles, name = 'articles')
]