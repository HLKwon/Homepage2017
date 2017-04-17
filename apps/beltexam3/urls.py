from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^quote$', views.quote),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^add_to_list/(?P<id>\d+)$', views.add_to_list, name='add_to_list'),
    url(r'^remove_from_list/(?P<id>\d+)$', views.remove_from_list, name='remove_from_list'),
    url(r'^users/(?P<id>\d+)$', views.users, name='users'),
]
