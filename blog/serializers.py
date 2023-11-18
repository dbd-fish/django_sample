from rest_framework import serializers
from .models import ArticleTag, PrivateArticle, JobArticle

class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        # これで全てのカラムを指定できる
        fields = '__all__'

class PrivateArticleSerializer(serializers.ModelSerializer):
    private_tag_names = ArticleTagSerializer(many=True)

    class Meta:
        model = PrivateArticle
        fields = '__all__'

class JobArticleSerializer(serializers.ModelSerializer):
    job_tag_names = ArticleTagSerializer(many=True)

    class Meta:
        model = JobArticle
        fields = '__all__'