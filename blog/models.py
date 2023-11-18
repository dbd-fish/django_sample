# blog/models.py

from django.db import models
from shortuuidfield import ShortUUIDField


class ArticleTag(models.Model):
    """タグ一覧"""
    tag_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        """デフォルトのソート条件"""
        ordering = ['created_date']

class PrivateArticle(models.Model):
    """趣味関連記事"""
    article_id = ShortUUIDField(primary_key=True)
    # ForeignKeyではなくManyToManyFieldでArticleTagテーブルに存在するデータが複数個入るように設定できているはず
    # private_tag_id = models.ForeignKey(ArticleTag, on_delete=models.CASCADE, related_name="private_tag_id") 
    private_tag_names = models.ManyToManyField(ArticleTag)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


    class Meta:
        ordering = ['created_date']

class JobArticle(models.Model):
    """仕事関連記事"""
    article_id = ShortUUIDField(primary_key=True)
    # job_tag_id = models.ForeignKey(ArticleTag, on_delete=models.CASCADE, related_name="private_tag_id") 
    job_tag_names = models.ManyToManyField(ArticleTag)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']