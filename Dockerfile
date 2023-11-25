# ベースイメージを指定
FROM python:3.12.0

# 作業ディレクトリを設定
WORKDIR /app

# Poetryのインストール
RUN pip install poetry

# Poetryのパスの設定
ENV PATH /root/.local/bin:$PATH

# Poetryが仮想環境を生成しないようにする
RUN poetry config virtualenvs.create false

# 依存パッケージをコピーしてインストール
COPY pyproject.toml poetry.lock /app/
RUN poetry install

# プロジェクトのファイルをコピー
COPY . /app/

# ポートを公開
EXPOSE 8000

# Djangoの開発用サーバを起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
