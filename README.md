# 大事な作業メモ
環境立ち上げ
docker-compose up

開発環境のURL
http://localhost:8000/

DjangoのログインURL
http://localhost:8000/admin/auth/user/add/

PgAdminのURL
http://localhost:5050/browser/

# 後でやることメモ
WARNING: アカウントやパスワードはテスト用なので後で書き換える


# メモ
djangoの練習

djangoの立ち上げコマンド
docker-compose run web django-admin startproject django_sample .

コンテナ終了
docker-compose down

コンテナ立ち上げ
docker-compose up -d

コンテナビルド
docker-compose up --build

WARNING: アカウントやパスワードはテスト用なので後で書き換える


DBのルートアカウント
Username (leave blank to use 'root'): root
Email address: test@test.com
Password: password
Password (again): 
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

Pgadmin4の接続手順
```
ログイン画面が表示されます。ここで、先ほど指定した PGADMIN_DEFAULT_EMAIL と PGADMIN_DEFAULT_PASSWORD を使用してログインします。

ログインしたら、左側のナビゲーションパネルで「Servers」を展開し、「PostgreSQL」を右クリックします。

「Create」を選択し、「Server...」をクリックします。

新しいサーバーの設定画面が表示されます。以下の情報を入力します：

Name: 任意の名前を入力します（例: My PostgreSQL Server）。
Connection タブ:
Host name/address: PostgreSQL サーバーのホスト名または IP アドレスを入力します。通常は Docker Compose ファイル内で指定したコンテナ名（例: db）が使えます。
Port: PostgreSQL のポート番号 (デフォルトは 5432)。
Maintenance database: POSTGRES_DB で指定したデータベース名（例: mydatabase）。
Username: POSTGRES_USER で指定したユーザー名（例: user）。
Password: POSTGRES_PASSWORD で指定したパスワード（例: password）。
「Save」をクリックして設定を保存します。
```
