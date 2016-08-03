from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

class BookmarkLV(ListView):
    model = Bookmark
    template_name = 'bookmark_list.html'

class BookmarkDV(DetailView):
    model = Bookmark
    template_name = 'bookmark_detail.html'

