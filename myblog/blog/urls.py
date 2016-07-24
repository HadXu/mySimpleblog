# coding:utf-8

from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.home'),
    url(r'^(?P<id>\d+)/$', 'blog.views.detail', name='detail'),
]
