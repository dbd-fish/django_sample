from django.test import TestCase
from datetime import datetime, timedelta
from .models import ArticleTag, PrivateArticle, JobArticle
from shortuuid import uuid

class BlogModelTestCase(TestCase):
    def setUp(self):
        # タグのテストデータ作成
        tag1 = ArticleTag.objects.create(tag_name='Tag1')
        tag2 = ArticleTag.objects.create(tag_name='Tag2')

        # 趣味関連記事のテストデータ作成
        private_article = PrivateArticle.objects.create(
            article_id=uuid(),
            title='Private Article 1',
            body='This is a private article.',
            created_date=datetime.now() - timedelta(days=5),
            updated_date=datetime.now(),
            is_deleted=False
        )
        private_article.private_tag_names.add(tag1)

        # 仕事関連記事のテストデータ作成
        job_article = JobArticle.objects.create(
            article_id=uuid(),
            title='Job Article 1',
            body='This is a job article.',
            created_date=datetime.now() - timedelta(days=3),
            updated_date=datetime.now(),
            is_deleted=False
        )
        job_article.job_tag_names.add(tag2)

    def test_data_created(self):
        # データが正しく作成されたかをテスト
        self.assertEqual(ArticleTag.objects.count(), 2)
        self.assertEqual(PrivateArticle.objects.count(), 1)
        self.assertEqual(JobArticle.objects.count(), 1)