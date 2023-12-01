import os
from django.core.management import call_command
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from datetime import datetime
import json
from .views import ArticleTagView, PrivateArticleView, JobArticleView
from unittest.mock import patch
from django.test import TestCase, Client


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
        response = self.client.post('/tags/', data, content_type='application/json')
        # ステータスコードが 201 Created であることを確認
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_article_tag_view_post_invalid(self):
        # 無効なデータで POST リクエストを作成
        data = {'invalid_field': 'some_value'}
        response = self.client.post('/tags/', data, content_type='application/json')
        # エラーレスポンスが返ってくることを確認
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

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
        response = self.client.post('/private_articles/', data, content_type='application/json')
        # ステータスコードが 201 Created であることを確認
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_private_article_view_post_invalid(self):
        # 無効なデータで POST リクエストを作成
        data = {'invalid_field': 'some_value'}
        response = self.client.post('/private_articles/', data, content_type='application/json')
        # エラーレスポンスが返ってくることを確認
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

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
            "job_tag_names": "JobTag1, JobTag2",
            "title": "Job Article Title",
            "body": "Job Article Body"
        }
        response = self.client.post('/job_articles/', data, content_type='application/json')
        # ステータスコードが 201 Created であることを確認
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_job_article_view_post_invalid(self):
        # 無効なデータで POST リクエストを作成
        data = {'invalid_field': 'some_value'}
        response = self.client.post('/job_articles/', data, content_type='application/json')
        # エラーレスポンスが返ってくることを確認
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)