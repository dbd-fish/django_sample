# blog/models.py

from django.core.exceptions import ValidationError
from django.db import models
from shortuuidfield import ShortUUIDField


class ArticleTag(models.Model):
    """タグ一覧"""

    TAG_TYPE_CHOICES = (
        (1, 'Private'),
        (2, 'Job'),
    )
    tag_name = models.CharField(max_length=50, primary_key=True)
    tag_type = models.IntegerField(choices=TAG_TYPE_CHOICES, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']

class PrivateArticle(models.Model):
    """趣味関連記事"""
    article_id = ShortUUIDField(primary_key=True)
    private_tag_names = models.CharField(max_length=255, default="default_value")
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']

    def clean(self):
        # カンマで区切られたタグをリストに変換
        tag_names = [tag.strip() for tag in self.private_tag_names.split(',')]

        # 各タグがArticleTagに存在するか確認
        for tag_name in tag_names:
            if not ArticleTag.objects.filter(tag_name=tag_name).exists():
                raise ValidationError({'private_tag_names': f'Tag {tag_name} does not exist in ArticleTag table.'})

class JobArticle(models.Model):
    """仕事関連記事"""

    article_id = ShortUUIDField(primary_key=True)
    job_tag_names = models.CharField(max_length=255, default="default_value")
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']

    def clean(self):
        tag_names = [tag.strip() for tag in self.job_tag_names.split(',')]
        for tag_name in tag_names:
            if not ArticleTag.objects.filter(tag_name=tag_name).exists():
                raise ValidationError({'job_tag_names': f'Tag {tag_name} does not exist in ArticleTag table.'})
