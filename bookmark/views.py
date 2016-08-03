from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

class BookmarkLV(ListView):
    model = Bookmark
    context_object_name = 'bookmark_list'
    template_name = 'bookmark/bookmark_list.html'

class BookmarkDV(DetailView):
    model = Bookmark
    context_object_name = 'bookmark_detail'
    template_name = 'bookmark/bookmark_detail.html'

