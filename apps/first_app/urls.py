from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^projects$', views.projects),
    url(r'^contact$', views.contact),
    url(r'^test$', views.test),
]
