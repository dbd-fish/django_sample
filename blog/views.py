# views.py
import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .logging_config import setup_logging  # 既存のlogging_configをインポート
from .models import ArticleTag, JobArticle, PrivateArticle
from .serializers import (
    ArticleTagSerializer,
    JobArticleSerializer,
    PrivateArticleSerializer,
)

# インポート時にログ設定を行う
setup_logging()

# ロギングの例
logger = logging.getLogger(__name__)


class ArticleTagView(APIView):
    """
    タグに関するAPI

    クエリパラメータ:
    - req: データ取得の条件を指定します。
    - tag_type: タグの種類を指定します。

    GETメソッド:
    - 'req'と'tag_type'パラメータが指定された場合は該当のデータを取得
    - 上記以外の場合は全データを取得

    POSTメソッド:
    - データを新規作成
    """

    def get(self, request, *args, **kwargs):
        try:
            # ログを追加（関数開始）
            logging.info("ArticleTagView.get start")

            # クエリパラメータ 'req' と 'tag_type' を取得
            req_param = request.query_params.get("req", None)
            tag_type_param = request.query_params.get("tag_type", None)
            logging.debug(f"ArticleTagView.get req_param = {req_param}")
            logging.debug(f"ArticleTagView.get tag_type_param = {tag_type_param}")

            # クエリパラメータにより取得対象を分岐
            if req_param == "all":
                # 'req' パラメータが 'all' の場合は全データを取得
                tags = ArticleTag.objects.all()
            elif tag_type_param:
                # 'tag_type' パラメータが指定された場合は該当のデータを取得
                tags = ArticleTag.objects.filter(tag_type=tag_type_param)
            else:
                # 'req' パラメータが指定された場合はエラーレスポンス
                logging.error("ArticleTagView.get invalid request parameter")
                return Response(
                    {"error": "Invalid req parameter for this endpoint"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # シリアライザを使ってデータをJSONに変換
            serializer = ArticleTagSerializer(tags, many=True)
            logging.info(f"ArticleTagView.get serializer = {serializer}")

            # レスポンスを返す
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # 例外が発生した場合のログを追加
            logging.exception(f"ArticleTagView.get exception occurred: {str(e)}")
            # 例外が発生した場合はエラーレスポンス
            return Response(
                {"error": "An error occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        finally:
            # ログを追加（関数終了）
            logging.info("ArticleTagView.get end")

    def post(self, request, *args, **kwargs):
        try:
            # ログを追加（関数開始）
            logging.info("ArticleTagView.post start")

            # POSTされたデータをシリアライザに渡す
            serializer = ArticleTagSerializer(data=request.data)
            logging.info(f"ArticleTagView.post serializer.data = {serializer}")

            if serializer.is_valid():
                # バリデーションが通れば保存
                serializer.save()
                # 保存したデータをJSONで返す
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            # バリデーションに失敗した場合はエラーメッセージを返す
            logging.error("Validation failed for ArticleTagView POST request")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # 例外が発生した場合のログを追加
            logging.exception(f"ArticleTagView.post exception occurred: {str(e)}")
            # 例外が発生した場合はエラーレスポンス
            return Response(
                {"error": "An error occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        finally:
            # ログを追加（関数終了）
            logging.info("ArticleTagView.post end")


# PrivateArticleView の修正
class PrivateArticleView(APIView):
    """
    趣味関連記事に関するAPI

    クエリパラメータ:
    - req: データ取得の条件を指定します。

    GETメソッド:
    - 'req'パラメータが 'all' の場合は全データを取得
    - 'req' パラメータが指定された場合は該当のデータを取得
    - 上記以外の場合はエラーレスポンス

    POSTメソッド:
    - データを新規作成
    """

    def get(self, request, *args, **kwargs):
        try:
            logging.info("PrivateArticleView.get start")

            # クエリパラメータ 'req' を取得
            req_param = request.query_params.get("req", None)
            logging.debug(f"PrivateArticleView.get req_param = {req_param}")

            # 'req' パラメータにより取得対象を分岐
            if req_param == "all":
                # 'all' が指定された場合は全てのデータを取得
                articles = PrivateArticle.objects.all()
            elif req_param:
                # 'req' パラメータが指定された場合は該当のデータを取得
                articles = PrivateArticle.objects.filter(article_id=req_param)
            else:
                # 'req' パラメータが無効または指定されていない場合はエラーレスポンス
                logging.error("PrivateArticleView.get invalid request parameter")
                return Response(
                    {"error": "Invalid or missing req parameter"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # シリアライザを使ってデータをJSONに変換
            serializer = PrivateArticleSerializer(articles, many=True)
            logging.info(f"PrivateArticleView.get serializer = {serializer}")

            # レスポンスを返す
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # 例外が発生した場合のログを追加
            logging.exception(f"PrivateArticleView.get exception occurred: {str(e)}")
            # 例外が発生した場合はエラーレスポンス
            return Response(
                {"error": "An error occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        finally:
            # ログを追加（関数終了）
            logging.info("PrivateArticleView.get end")

    def post(self, request, *args, **kwargs):
        try:
            # ログを追加（関数開始）
            logging.info("PrivateArticleView.post start")

            # POSTされたデータをシリアライザに渡す
            serializer = PrivateArticleSerializer(data=request.data)
            logging.info(f"PrivateArticleView.post serializer.data = {serializer}")

            if serializer.is_valid():
                # バリデーションが通れば保存
                serializer.save()
                # 保存したデータをJSONで返す
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            # バリデーションに失敗した場合はエラーメッセージを返す
            logging.error("PrivateArticleView.get invalid request parameter")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # 例外が発生した場合のログを追加
            logging.exception(f"PrivateArticleView.post exception occurred: {str(e)}")
            # 例外が発生した場合はエラーレスポンス
            return Response(
                {"error": "An error occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        finally:
            # ログを追加（関数終了）
            logging.info("PrivateArticleView.post end")


# JobArticleView の修正
class JobArticleView(APIView):
    """
    仕事関連記事に関するAPI

    クエリパラメータ:
    - req: データ取得の条件を指定します。

    GETメソッド:
    - 'req'パラメータが 'all' の場合は全データを取得
    - 'req' パラメータが指定された場合は該当のデータを取得
    - 上記以外の場合はエラーレスポンス

    POSTメソッド:
    - データを新規作成
    """

    def get(self, request, *args, **kwargs):
        try:
            # ログを追加（関数開始）
            logging.info("JobArticleView.get start")

            # クエリパラメータ 'req' を取得
            req_param = request.query_params.get("req", None)
            logging.debug(f"JobArticleView.get req_param = {req_param}")

            # 'req' パラメータにより取得対象を分岐
            if req_param == "all":
                # 'all' が指定された場合は全てのデータを取得
                articles = JobArticle.objects.all()
            elif req_param:
                # 'req' パラメータが指定された場合は該当のデータを取得
                articles = JobArticle.objects.filter(article_id=req_param)
            else:
                # 'req' パラメータが無効または指定されていない場合はエラーレスポンス
                logging.error("JobArticleView.get invalid request parameter")
                return Response(
                    {"error": "Invalid or missing req parameter"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # シリアライザを使ってデータをJSONに変換
            serializer = JobArticleSerializer(articles, many=True)
            logging.info(f"JobArticleView.get serializer = {serializer}")

            # レスポンスを返す
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # 例外が発生した場合のログを追加
            logging.exception(f"JobArticleView.get exception occurred: {str(e)}")
            # 例外が発生した場合はエラーレスポンス
            return Response(
                {"error": "An error occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        finally:
            # ログを追加（関数終了）
            logging.info("JobArticleView.get end")

    def post(self, request, *args, **kwargs):
        try:
            # ログを追加（関数開始）
            logging.info("JobArticleView.post start")

            # POSTされたデータをシリアライザに渡す
            serializer = JobArticleSerializer(data=request.data)
            logging.info(f"PrivateArticleView.post serializer.data = {serializer}")

            if serializer.is_valid():
                # バリデーションが通れば保存
                serializer.save()
                # 保存したデータをJSONで返す
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            # バリデーションに失敗した場合はエラーメッセージを返す
            logging.error("Validation failed for JobArticleView POST request")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # 例外が発生した場合のログを追加
            logging.exception(f"JobArticleView.post exception occurred: {str(e)}")
            # 例外が発生した場合はエラーレスポンス
            return Response(
                {"error": "An error occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        finally:
            # ログを追加（関数終了）
            logging.info("JobArticleView.post end")
