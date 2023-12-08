# blog/admin.py

from django.contrib import admin

from .models import ArticleTag, JobArticle, PrivateArticle

admin.site.register(PrivateArticle)
admin.site.register(JobArticle)
admin.site.register(ArticleTag)
