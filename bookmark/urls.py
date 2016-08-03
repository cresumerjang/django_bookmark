from django.conf.urls import url, include
from django.views.generic import ListView
from bookmark.views import *

urlpatterns = [
    url(r'^$',  BookmarkLV.as_view(),name='index'),
]