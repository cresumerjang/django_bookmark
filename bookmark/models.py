from django.db import models
from django.core.urlresolvers import reverse, reverse_lazy

class Bookmark(models.Model):
    title = models.CharField('사이트명', max_length=100, blank=True, null=True)
    url = models.URLField('도메인', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bookmark:index')

