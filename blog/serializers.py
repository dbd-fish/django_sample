from rest_framework import serializers
from .models import ArticleTag, PrivateArticle, JobArticle

class ArticleTagSerializer(serializers.ModelSerializer):
    """
    ArticleTagモデルのシリアライザ

    フィールド:
    - タグの名前(tag_name)
    - タグの種類(tag_type)
    - 作成日時(created_date)
    - 更新日時(updated_date)
    - 論理削除フラグ(is_deleted)
    """

    class Meta:
        model = ArticleTag
        # これで全てのカラムを指定できる
        fields = '__all__'

class PrivateArticleSerializer(serializers.ModelSerializer):
    """
    PrivateArticleモデルのシリアライザ

    フィールド:
    - 記事ID(article_id)
    - プライベートタグの名前（カンマで区切られた文字列）(private_tag_names)
    - タイトル(title)
    - 本文(body)
    - 作成日時(created_date)
    - 更新日時(updated_date)
    - 論理削除フラグ(is_deleted)

    カスタムフィールド:
    - プライベートタグの名前をリストに変換するためのフィールド(private_tag_names_list)
    """

    # カンマで区切られたタグ名をリストに変換するためのフィールド
    private_tag_names_list = serializers.ListField(
        write_only=True,
        required=False,
        help_text="カンマで区切られたタグ名の文字列をリストに変換するためのフィールド"
    )

    class Meta:
        model = PrivateArticle
        fields = '__all__'

    def create(self, validated_data):
        # 新しいフィールド 'private_tag_names_list' を 'private_tag_names' にコピー
        validated_data['private_tag_names'] = ', '.join(validated_data.pop('private_tag_names_list', []))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # 新しいフィールド 'private_tag_names_list' を 'private_tag_names' にコピー
        validated_data['private_tag_names'] = ', '.join(validated_data.pop('private_tag_names_list', []))
        return super().update(instance, validated_data)

class JobArticleSerializer(serializers.ModelSerializer):
    """
    JobArticleモデルのシリアライザ

    フィールド:
    - 記事ID(article_id)
    - ジョブタグの名前（カンマで区切られた文字列）(job_tag_names)
    - タイトル(title)
    - 本文(body)
    - 作成日時(created_date)
    - 更新日時(updated_date)
    - 論理削除フラグ(is_deleted)

    カスタムフィールド:
    - ジョブタグの名前をリストに変換するためのフィールド(job_tag_names_list)
    """

    # カンマで区切られたタグ名をリストに変換するためのフィールド
    job_tag_names_list = serializers.ListField(
        write_only=True,
        required=False,
        help_text="カンマで区切られたタグ名の文字列をリストに変換するためのフィールド"
    )

    class Meta:
        model = JobArticle
        fields = '__all__'

    def create(self, validated_data):
        # 新しいフィールド 'job_tag_names_list' を 'job_tag_names' にコピー
        validated_data['job_tag_names'] = ', '.join(validated_data.pop('job_tag_names_list', []))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # 新しいフィールド 'job_tag_names_list' を 'job_tag_names' にコピー
        validated_data['job_tag_names'] = ', '.join(validated_data.pop('job_tag_names_list', []))
        return super().update(instance, validated_data)
