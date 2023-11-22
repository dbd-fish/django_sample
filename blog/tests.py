import os
from django.core.management import call_command
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from datetime import datetime
import json
from blog.models import ArticleTag, PrivateArticle, JobArticle


class BlogApiTest(APITestCase):
    def setUp(self):
        # カレントディレクトリを移動
        current_directory = os.path.dirname(os.path.abspath(__file__))
        os.chdir(current_directory)

        # フィクスチャを読み込む
        call_command('loaddata', 'dummy_data.json')

    def test_get_private_articles_all(self):
        # 趣味関連記事の全データを取得するテスト
        url = reverse('private-article-list')
        response = self.client.get(url, {'req': 'all'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), PrivateArticle.objects.count())

    def test_get_private_articles_by_id(self):
        # 趣味関連記事をIDで取得するテスト
        article_id = 'PrivateArticle1'
        url = reverse('private-article-list')
        response = self.client.get(url, {'req': article_id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['article_id'], article_id)

    def test_get_private_articles_invalid_req_param(self):
        # 無効なreqパラメータでエラーを返すテスト
        url = reverse('private-article-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_private_articles(self):
        # 趣味関連記事を新規作成するテスト
        url = reverse('private-article-list')
        data = {'article_id': 'NewPrivateArticle', 'private_tag_names': 'Private1', 'title': 'New Private Article', 'body': 'Body of New Private Article'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PrivateArticle.objects.filter(article_id='NewPrivateArticle').count(), 1)

    def test_get_tags_all(self):
        # タグの全データを取得するテスト
        url = reverse('tag-list')
        response = self.client.get(url, {'req': 'all'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), ArticleTag.objects.count())

    def test_get_tags_by_type(self):
        # タグの種類でフィルタリングしてデータを取得するテスト
        url = reverse('tag-list')
        response = self.client.get(url, {'tag_type': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), ArticleTag.objects.filter(tag_type=1).count())

    def test_get_tags_invalid_req_param(self):
        # 無効なreqパラメータでエラーを返すテスト
        url = reverse('tag-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



    def test_get_job_articles_all(self):
        # 仕事関連記事の全データを取得するテスト
        url = reverse('job-article-list')
        response = self.client.get(url, {'req': 'all'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), JobArticle.objects.count())

    def test_get_job_articles_by_id(self):
        # 仕事関連記事をIDで取得するテスト
        article_id = 'JobArticle1'
        url = reverse('job-article-list')
        response = self.client.get(url, {'req': article_id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['article_id'], article_id)

    def test_get_job_articles_invalid_req_param(self):
        # 無効なreqパラメータでエラーを返すテスト
        url = reverse('job-article-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_post_job_articles(self):
    #     # 仕事関連記事を新規作成するテスト
    #     url = reverse('job-article-list')
    #     data = {'article_id': 'NewJobArticle', 'job_tag_names': 'Job1', 'title': 'New Job Article', 'body': 'Body of New Job Article'}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(JobArticle.objects.filter(article_id='NewJobArticle').count(), 1)

    def test_post_job_articles(self):
        # 新しいジョブ記事のデータ
        new_job_article_data = {
            "article_id": "NewJobArticle",
            "job_tag_names": "Job1, Job2",  
            "title": "New Job Article",
            "body": "Body of New Job Article"
        }

        # データベースに新しい記事が存在しないことを確認
        self.assertEqual(JobArticle.objects.filter(article_id='NewJobArticle').count(), 0)

        # 新しいジョブ記事を作成するための POST リクエストを送信
        response = self.client.post('/job_articles/', new_job_article_data, format='json')

        # POST リクエストが成功したことを確認
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # データベースに新しい記事が存在することを確認
        self.assertEqual(JobArticle.objects.filter(article_id='NewJobArticle').count(), 1)