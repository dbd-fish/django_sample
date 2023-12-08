# blog/models.py
from typing import List, Tuple

from django.core.exceptions import ValidationError
from django.db import models
from shortuuidfield import ShortUUIDField


class ArticleTag(models.Model):
    """
    タグ一覧のモデル

    フィールド:
    - タグの名前(tag_name)
    - タグの種類(tag_type)
    - 作成日時(created_date)
    - 更新日時(updated_date)
    - 論理削除フラグ(is_deleted)
    """

    TAG_TYPE_CHOICES: List[Tuple[int, str]] = [
        (1, "Private"),
        (2, "Job"),
    ]

    tag_name: models.CharField = models.CharField(max_length=50, primary_key=True)
    tag_type: models.IntegerField = models.IntegerField(choices=TAG_TYPE_CHOICES, default=1)
    created_date: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_date: models.DateTimeField = models.DateTimeField(auto_now=True)
    is_deleted: models.BooleanField = models.BooleanField(default=False)

    class Meta:
        ordering: List[str] = ["created_date"]


class PrivateArticle(models.Model):
    """
    趣味関連記事のモデル

    フィールド:
    - 記事ID(article_id)
    - プライベートタグの名前（カンマで区切られた文字列）(private_tag_names)
    - タイトル(title)
    - 本文(body)
    - 作成日時(created_date)
    - 更新日時(updated_date)
    - 論理削除フラグ(is_deleted)
    """

    article_id: ShortUUIDField = ShortUUIDField(primary_key=True)
    private_tag_names: models.CharField = models.CharField(max_length=255, default="default_value")
    title: models.CharField = models.CharField(max_length=100)
    body: models.TextField = models.TextField()
    created_date: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_date: models.DateTimeField = models.DateTimeField(auto_now=True)
    is_deleted: models.BooleanField = models.BooleanField(default=False)

    class Meta:
        ordering: List[str] = ["created_date"]

    def clean(self) -> None:
        """
        カンマで区切られたタグ名をリストに変換し、
        各タグがArticleTagに存在するか確認する。

        Raises:
            ValidationError: タグがArticleTagに存在しない場合に発生
        """
        # カンマで区切られたタグをリストに変換
        tag_names: List[str] = [tag.strip() for tag in self.private_tag_names.split(", ")]

        # カンマが含まれていない場合は正常終了
        if not any(tag_names):
            return

        # 各タグがArticleTagに存在するか確認
        for tag_name in tag_names:
            if not ArticleTag.objects.filter(tag_name=tag_name).exists():
                raise ValidationError(
                    {
                        "private_tag_names": f"Tag {tag_name} does not exist in ArticleTag table."
                    }
                )
        return


class JobArticle(models.Model):
    """
    仕事関連記事のモデル

    フィールド:
    - 記事ID(article_id)
    - ジョブタグの名前（カンマで区切られた文字列）(job_tag_names)
    - タイトル(title)
    - 本文(body)
    - 作成日時(created_date)
    - 更新日時(updated_date)
    - 論理削除フラグ(is_deleted)
    """

    article_id: ShortUUIDField = ShortUUIDField(primary_key=True)
    job_tag_names: models.CharField = models.CharField(max_length=255, default="default_value")
    title: models.CharField = models.CharField(max_length=100)
    body: models.TextField = models.TextField()
    created_date: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_date: models.DateTimeField = models.DateTimeField(auto_now=True)
    is_deleted: models.BooleanField = models.BooleanField(default=False)

    class Meta:
        ordering: List[str] = ["created_date"]

    def clean(self) -> None:
        """
        カンマで区切られたタグ名をリストに変換し、
        各タグがArticleTagに存在するか確認する。

        Raises:
            ValidationError: タグがArticleTagに存在しない場合に発生
        """
        # カンマで区切られたタグをリストに変換
        tag_names: List[str] = [tag.strip() for tag in self.job_tag_names.split(", ")]

        # カンマが含まれていない場合は正常終了
        if not any(tag_names):
            return

        # 各タグがArticleTagに存在するか確認
        for tag_name in tag_names:
            if not ArticleTag.objects.filter(tag_name=tag_name).exists():
                raise ValidationError(
                    {
                        "job_tag_names": f"Tag {tag_name} does not exist in ArticleTag table."
                    }
                )
