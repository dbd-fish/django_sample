# blog/urls.py
"""
URL configuration for django_sample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog.views import ArticleTagView, JobArticleView, PrivateArticleView

urlpatterns = [
    path("admin/", admin.site.urls),
    # タグ一覧に対するURLパターン
    path("tags/", ArticleTagView.as_view(), name="tag-list"),
    # 趣味関連記事一覧に対するURLパターン
    path("private_articles/", PrivateArticleView.as_view(), name="private-article-list"),
    # 仕事関連記事一覧に対するURLパターン
    path("job_articles/", JobArticleView.as_view(), name="job-article-list"),
]
