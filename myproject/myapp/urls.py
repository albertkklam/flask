from django.conf.urls import include, url
from . import views, models
from django.views.generic import TemplateView, ListView

urlpatterns = [
	url(r'^hello', views.hello, name = 'hello'),
	url(r'^morning/', views.morning, name = 'morning'),
	url(r'^number/(\d+)/', views.randNum, name = 'number'),
	url(r'^fraction/(\d{1,4})/(\d{1,4})', views.randFrac, name = 'fraction'),
	url(r'^static/', TemplateView.as_view(template_name = 'myapp/static.html')),
	url(r'^dreamreals/', ListView.as_view(model = models.Dreamreal, template_name = 'myapp/dreamreal_list.html')),
	url(r'^connection/',TemplateView.as_view(template_name = 'myapp/login.html')),
	url(r'^login/', views.login, name = 'login'),
]