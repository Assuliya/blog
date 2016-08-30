from __future__ import unicode_literals
from django.db import models

class Entry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=64)
    text = models.TextField()
    published = models.BooleanField(db_index=True, default=True)

    def __unicode__(self):
        return u"%s - %s" % (self.title, self.created)
