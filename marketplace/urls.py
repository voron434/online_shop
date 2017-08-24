from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.clothes_list, name='clothes_list'),
    url(r'^drafts/$', views.clothes_draft_list, name='clothes_draft_list'),
    url(r'^clothes/new/$', views.clothes_new, name='clothes_new'),
    url(r'^clothes/(?P<pk>[0-9]+)/$', views.clothes_detail, name='clothes_detail'),
    url(r'^clothes/(?P<pk>[0-9]+)/edit/$', views.clothes_edit, name='clothes_edit'),
    url(r'^clothes/(?P<pk>\d+)/publish/$', views.clothes_publish, name='clothes_publish'),
    url(r'^clothes/filter/mens$', views.filter_clothes_mens, name='filter_clothes_mens'),
    url(r'^clothes/filter/womens$', views.filter_clothes_womens, name='filter_clothes_womens'),
    url(r'^clothes/filter/child$', views.filter_clothes_child, name='filter_clothes_child'),

]