from django.conf.urls import url, include
from django.views.generic import ListView
from bookmark.views import *

urlpatterns = [
    url(r'^$', BookmarkMain.as_view(), name='main'),
    url(r'^list/$', BookmarkLV.as_view(), name='list'),
    url(r'^detail/(?P<pk>[0-9]+)/$',  BookmarkDV.as_view(), name='detail'),

    url(r'^tag/$', BookmarkTV.as_view(), name='tag_cloud'),
    url(r'^tag/(?P<tag>[^/]+(?u))/$', BookmarkTOL.as_view(), name='tag_object_list'),
]