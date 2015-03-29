# -*- coding: utf-8 -*-
# core.models

from google.appengine.ext import db

# Create your models here.


class Article(db.Model):
    title = db.StringProperty()
    updated_at = db.DateTimeProperty(auto_now=True)
    created_at = db.DateTimeProperty(auto_now_add=True)

    def __unicode__(self):
        return self.title
