from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from wines import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^$', views.index, name='home'),
]