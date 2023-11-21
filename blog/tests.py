# blog/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import ArticleTag, PrivateArticle, JobArticle
from .serializers import ArticleTagSerializer, PrivateArticleSerializer, JobArticleSerializer

class BaseAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # ArticleTagの初期データ
        ArticleTag.objects.create(tag_name='Private1', tag_type=1, created_date='2023-01-01T00:00:00Z', updated_date='2023-01-01T00:00:00Z', is_deleted=False)
        ArticleTag.objects.create(tag_name='Private2', tag_type=1, created_date='2023-01-02T00:00:00Z', updated_date='2023-01-02T00:00:00Z', is_deleted=False)
        ArticleTag.objects.create(tag_name='Job1', tag_type=2, created_date='2023-01-03T00:00:00Z', updated_date='2023-01-03T00:00:00Z', is_deleted=False)
        ArticleTag.objects.create(tag_name='Job2', tag_type=2, created_date='2023-01-04T00:00:00Z', updated_date='2023-01-04T00:00:00Z', is_deleted=False)

        # PrivateArticleの初期データ
        PrivateArticle.objects.create(article_id='PrivateArticle1', private_tag_names='Private1, Private2', title='Private Article 1', body='Body of Private Article 1', created_date='2023-01-01T00:00:00Z', updated_date='2023-01-01T00:00:00Z', is_deleted=False)
        PrivateArticle.objects.create(article_id='PrivateArticle2', private_tag_names='Private1, Private2', title='Private Article 2', body='Body of Private Article 2', created_date='2023-01-02T00:00:00Z', updated_date='2023-01-02T00:00:00Z', is_deleted=False)
        PrivateArticle.objects.create(article_id='PrivateArticle3', private_tag_names='Private2', title='Private Article 3', body='Body of Private Article 3', created_date='2023-01-03T00:00:00Z', updated_date='2023-01-03T00:00:00Z', is_deleted=False)
        PrivateArticle.objects.create(article_id='PrivateArticle4', private_tag_names='Private1', title='Private Article 4', body='Body of Private Article 4', created_date='2023-01-04T00:00:00Z', updated_date='2023-01-04T00:00:00Z', is_deleted=False)

        # JobArticleの初期データ
        JobArticle.objects.create(article_id='JobArticle1', job_tag_names='Job1, Job2', title='Job Article 1', body='Body of Job Article 1', created_date='2023-01-01T00:00:00Z', updated_date='2023-01-01T00:00:00Z', is_deleted=False)
        JobArticle.objects.create(article_id='JobArticle2', job_tag_names='Job1', title='Job Article 2', body='Body of Job Article 2', created_date='2023-01-02T00:00:00Z', updated_date='2023-01-02T00:00:00Z', is_deleted=False)
        JobArticle.objects.create(article_id='JobArticle3', job_tag_names='Job2', title='Job Article 3', body='Body of Job Article 3', created_date='2023-01-03T00:00:00Z', updated_date='2023-01-03T00:00:00Z', is_deleted=False)
        JobArticle.objects.create(article_id='JobArticle4', job_tag_names='Job1, Job2', title='Job Article 4', body='Body of Job Article 4', created_date='2023-01-04T00:00:00Z', updated_date='2023-01-04T00:00:00Z', is_deleted=False)

class ArticleTagAPITestCase(BaseAPITestCase):
    def test_create_article_tag(self):
        # ArticleTagを作成するAPIのテスト
        response = self.client.post('/api/article-tag/', {'tag_name': 'TestTag', 'tag_type': 1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ArticleTag.objects.count(), 1)
        self.assertEqual(ArticleTag.objects.get().tag_name, 'TestTag')

    def test_get_all_article_tags(self):
        # 全てのArticleTagを取得するAPIのテスト
        response = self.client.get('/api/article-tag/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_get_filtered_article_tags(self):
        # フィルタリングされたArticleTagを取得するAPIのテスト
        response = self.client.get('/api/article-tag/', {'req': 'Private1', 'tag_type': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['tag_name'], 'Private1')

class PrivateArticleAPITestCase(BaseAPITestCase):
    def test_create_private_article(self):
        # PrivateArticleを作成するAPIのテスト
        response = self.client.post('/api/private-article/', {'private_tag_names': 'Private1, Private2', 'title': 'Test Article', 'body': 'Article Body'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PrivateArticle.objects.count(), 1)
        self.assertEqual(PrivateArticle.objects.get().title, 'Test Article')

    def test_get_all_private_articles(self):
        # 全てのPrivateArticleを取得するAPIのテスト
        response = self.client.get('/api/private-article/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
