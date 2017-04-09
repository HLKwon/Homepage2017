from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^projects$', views.projects),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^test$', views.test),
]
