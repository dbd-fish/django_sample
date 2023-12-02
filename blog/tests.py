import os
from django.core.management import call_command
from rest_framework.test import APITestCase
from rest_framework import status
from django.test import Client
from .models import ArticleTag, PrivateArticle, JobArticle


class BlogApiTest(APITestCase):
    def setUp(self):
        self.client = Client()

        # カレントディレクトリを移動
        current_directory = os.path.dirname(os.path.abspath(__file__))
        os.chdir(current_directory)

        # フィクスチャを読み込む
        call_command('loaddata', 'dummy_data.json')

    # ArticleTagView のテストケース
    def test_article_tag_view_get_all(self):
        # 'req=all' で GET リクエストを作成
        response = self.client.get('/tags/?req=all')
        # ステータスコードが 200 OK であることを確認
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_article_tag_view_get_filtered(self):
        # フィルター付き GET リクエストを作成
        response = self.client.get('/tags/?req=some_req&tag_type=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_article_tag_view_get_invalid_param(self):
        # 不正なパラメータで GET リクエストを作成
        response = self.client.get('/tags/?invalid_param=value')
        # エラーレスポンスが返ってくることを確認
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_article_tag_view_post_valid(self):
        # 有効なデータで POST リクエストを作成
        data = {
            "tag_name": "UnitTest Tag",
            "tag_type": 1
        }
        initial_count = ArticleTag.objects.count()
        response = self.client.post('/tags/', data, content_type='application/json')
        # ステータスコードが 201 Created であることを確認
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # アサーション: タグがデータベースに存在することを確認
        self.assertTrue(ArticleTag.objects.filter(tag_name='UnitTest Tag').exists())
        # アサーション: レコード数が1増加していることを確認
        self.assertEqual(ArticleTag.objects.count(), initial_count + 1)

    def test_article_tag_view_post_invalid(self):
        # 無効なデータで POST リクエストを作成
        data = {'invalid_field': 'some_value'}
        initial_count = ArticleTag.objects.count()
        response = self.client.post('/tags/', data, content_type='application/json')
        # エラーレスポンスが返ってくることを確認
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # アサーション: データベースにタグが追加されていないことを確認
        self.assertFalse(ArticleTag.objects.filter(tag_name='some_value').exists())
        # アサーション: レコード数が変化していないことを確認
        self.assertEqual(ArticleTag.objects.count(), initial_count)

    # PrivateArticleView のテストケース
    def test_private_article_view_get_all(self):
        response = self.client.get('/private_articles/?req=all')
        # ステータスコードが 200 OK であることを確認
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_private_article_view_get_filtered(self):
        # フィルター付き GET リクエストを作成
        response = self.client.get('/private_articles/?req=some_req')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_private_article_view_get_invalid_param(self):
        # 不正なパラメータで GET リクエストを作成
        response = self.client.get('/private_articles/?invalid_param=value')
        # エラーレスポンスが返ってくることを確認
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_private_article_view_post_valid(self):
        # 有効なデータで POST リクエストを作成
        data = {
            "private_tag_names": "Tag1, Tag2",
            "title": "Private Article Title",
            "body": "Private Article Body"
        }
        initial_count = PrivateArticle.objects.count()
        response = self.client.post('/private_articles/', data, content_type='application/json')
        # ステータスコードが 201 Created であることを確認
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # アサーション: プライベート記事がデータベースに存在することを確認
        self.assertTrue(PrivateArticle.objects.filter(title='Private Article Title').exists())
        # アサーション: レコード数が1増加していることを確認
        self.assertEqual(PrivateArticle.objects.count(), initial_count + 1)

    def test_private_article_view_post_invalid(self):
        # 無効なデータで POST リクエストを作成
        data = {'invalid_field': 'some_value'}
        initial_count = PrivateArticle.objects.count()
        response = self.client.post('/private_articles/', data, content_type='application/json')
        # エラーレスポンスが返ってくることを確認
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # アサーション: レコード数が変化していないことを確認
        self.assertEqual(PrivateArticle.objects.count(), initial_count)

    # JobArticleView のテストケース
    def test_job_article_view_get_all(self):
        response = self.client.get('/job_articles/?req=all')
        # ステータスコードが 200 OK であることを確認
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_job_article_view_get_filtered(self):
        # フィルター付き GET リクエストを作成
        response = self.client.get('/job_articles/?req=some_req')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_job_article_view_get_invalid_param(self):
        # 不正なパラメータで GET リクエストを作成
        response = self.client.get('/job_articles/?invalid_param=value')
        # エラーレスポンスが返ってくることを確認
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_job_article_view_post_valid(self):
        # 有効なデータで POST リクエストを作成
        data = {
            "job_tag_names": "Tag1, Tag2",
            "title": "Job Article Title",
            "body": "Job Article Body"
        }
        initial_count = JobArticle.objects.count()
        response = self.client.post('/job_articles/', data, content_type='application/json')
        # ステータスコードが 201 Created であることを確認
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # アサーション: ジョブ記事がデータベースに存在することを確認
        self.assertTrue(JobArticle.objects.filter(title='Job Article Title').exists())
        # アサーション: レコード数が1増加していることを確認
        self.assertEqual(JobArticle.objects.count(), initial_count + 1)

    def test_job_article_view_post_invalid(self):
        # 無効なデータで POST リクエストを作成
        data = {'invalid_field': 'some_value'}
        initial_count = JobArticle.objects.count()
        response = self.client.post('/job_articles/', data, content_type='application/json')
        # エラーレスポンスが返ってくることを確認
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # アサーション: レコード数が変化していないことを確認
        self.assertEqual(JobArticle.objects.count(), initial_count)
