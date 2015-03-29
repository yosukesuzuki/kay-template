# -*- coding: utf-8 -*-

from kay.ext.testutils.gae_test_base import GAETestBase

from core.models import Article


class GetArticleTest(GAETestBase):
    CLEANUP_USED_KIND = True
    USE_PRODUCTION_STUBS = True

    def test_put_article(self):
        entity = Article(key_name='test1', title='test_title1')
        entity.put()
        entity_for_assert = Article.get_by_key_name('test1')
        self.assertEquals(entity_for_assert.title, 'test_title1')
