# -*- coding: utf-8 -*-

from kay.generics import crud
from kay.routing import (
    ViewGroup, Rule
)

from core.models import Article
from admin.forms import ArticleForm


class ArticleCRUDViewGroup(crud.CRUDViewGroup):
    model = Article
    form = ArticleForm


view_groups = [
    ViewGroup(
        Rule('/', endpoint='index', view='admin.views.index'),
    ),
    ArticleCRUDViewGroup(),
]
