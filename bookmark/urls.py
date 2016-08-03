from django.conf.urls import url, include
from django.views.generic import ListView
from bookmark.views import *

urlpatterns = [
    url(r'^$', BookmarkLV.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$',  BookmarkDV.as_view(), name='detail'),
]