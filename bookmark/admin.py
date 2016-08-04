from django.contrib import admin
from bookmark.models import Bookmark

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'tag')

admin.site.register(Bookmark, BookmarkAdmin)
