# ベースイメージを指定
FROM python:3.12.0

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# psycopg2をインストール
RUN pip install psycopg2-binary

# プロジェクトのファイルをコピー
COPY . /app/

# ポートを公開
EXPOSE 8000

# Djangoの開発用サーバを起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]