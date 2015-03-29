# -*- coding: utf-8 -*-

from kay.utils.forms.modelform import ModelForm

from core.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
