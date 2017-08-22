from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.clothes_list, name='clothes_list'),
    url(r'^clothes/new/$', views.clothes_new, name='clothes_new'),
    url(r'^clothes/(?P<pk>[0-9]+)/$', views.clothes_detail, name='clothes_detail'),
    url(r'^clothes/(?P<pk>[0-9]+)/edit/$', views.clothes_edit, name='clothes_edit'),
]