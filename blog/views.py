from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ArticleTag, PrivateArticle, JobArticle
from .serializers import ArticleTagSerializer, PrivateArticleSerializer, JobArticleSerializer

class ArticleTagListView(APIView):
    def get(self, request, *args, **kwargs):
        # クエリパラメータ取得をする場合は下記のように
        # タグ一覧を取得
        tags = ArticleTag.objects.all()
        # シリアライザを使ってデータをJSONに変換
        serializer = ArticleTagSerializer(tags, many=True)
        # レスポンスを返す
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # POSTされたデータをシリアライザに渡す
        serializer = ArticleTagSerializer(data=request.data)
        if serializer.is_valid():
            # バリデーションが通れば保存
            serializer.save()
            # 保存したデータをJSONで返す
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # バリデーションに失敗した場合はエラーメッセージを返す
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrivateArticleListView(APIView):
    def get(self, request, *args, **kwargs):
        # 趣味関連記事一覧を取得
        articles = PrivateArticle.objects.all()
        # シリアライザを使ってデータをJSONに変換
        serializer = PrivateArticleSerializer(articles, many=True)
        # レスポンスを返す
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # POSTされたデータをシリアライザに渡す
        serializer = PrivateArticleSerializer(data=request.data)
        if serializer.is_valid():
            # バリデーションが通れば保存
            serializer.save()
            # 保存したデータをJSONで返す
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # バリデーションに失敗した場合はエラーメッセージを返す
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobArticleListView(APIView):
    def get(self, request, *args, **kwargs):
        # 仕事関連記事一覧を取得
        articles = JobArticle.objects.all()
        # シリアライザを使ってデータをJSONに変換
        serializer = JobArticleSerializer(articles, many=True)
        # レスポンスを返す
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # POSTされたデータをシリアライザに渡す
        serializer = JobArticleSerializer(data=request.data)
        if serializer.is_valid():
            # バリデーションが通れば保存
            serializer.save()
            # 保存したデータをJSONで返す
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # バリデーションに失敗した場合はエラーメッセージを返す
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
