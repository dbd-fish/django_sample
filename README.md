# 直近でやること
単体テストが動かない問題の解決。
    POST時にtag_namesが入力されない

あわよくばファイル保存。
URLの自動生成できる？
デバック環境を整える。


# 大事な作業メモ
コンテナビルド
docker-compose up --build

環境立ち上げ
docker-compose up
docker-compose up -d

コンテナに入る
docker container exec -it django_sample-web-1 bash

開発環境のURL
http://localhost:8000/

DjangoのログインURL
http://localhost:8000/admin/auth/user/add/

PgAdminのURL
http://localhost:5050/browser/

インストールしたものを確認
pip list

テーブルを変更した場合の儀式
    新しいモデルをもとにマイグレーションファイルの生成
    python manage.py makemigrations
    マイグレーションファイルを実行して、新しいモデルをDBに反映させる
    python manage.py migrate
    ダミーデータの挿入
    python manage.py loaddata dummy_data.json

    注意：テーブル内のデータも削除したい場合はDBを削除する必要あり

APIの動作確認
    http://localhost:8000/tags/?req=all
    http://localhost:8000/tags/?tag_type=1
    http://localhost:8000/job_articles/?req=JobArticle1
    http://localhost:8000/private_articles/?req=PrivateArticle1



単体テストの実行
python manage.py test blog.tests

# 設計メモ
DjangoはアプリごとにURLやテーブルを作るっぽい
→今回の場合はブログ用APIを一か所にまとめる
→viewやhtmlファイルについてもアプリ配下においておく
→静的ファイル(CSSなど)はアプリ配下のstaticフォルダ内で管理する

### テーブル名
- 趣味記事一覧テーブル(仕事記事一覧テーブルも同様)
    記事ID(shortuuidにしたい。shortuuidをURLパスにしたい。)
    趣味タグID(複数タグを考慮してCSV形式かな？)
    記事タイトル
    記事本文？(概要が別項目であると望ましいとりあえず本文だけにする)
    記事作成日
    記事更新日
    論理削除フラグ

- タグ一覧テーブル(仕事と趣味で共用)
    タグID(普通のAutoIncrementでいいか)
    カテゴリID(仕事タグなのか趣味タグなのか判別)
    タグ名
    作成日
    更新日
    論理削除フラグ

### API
- 趣味記事リスト抽出処理(仕事記事リスト抽出処理)
    趣味記事一覧テーブルからID、タグ、記事タイトル、本文を抽出する。
- 単一趣味記事抽出処理(単一仕事記事抽出処理)
    趣味記事一覧テーブルから特定IDの全項目を抽出する。
    - 記事更新日で降順にする
- 趣味タグ一覧抽出処理(仕事タグ一覧抽出処理)
    趣味タグ一覧を抽出する。
    - 件数が多いものを一番上に並べる



# 後でやることメモ
WARNING: アカウントやパスワードはテスト用なので後で書き換える

Peetryのデフォルトの仮想環境をONにした方がいい？
データベース名、ユーザ名、パスワードを適切なものに設定する。

# メモ
docker container exec -it django_sample-web-1 bash

python manage.py startapp blog

djangoの練習

djangoの立ち上げコマンド
docker-compose run web django-admin startproject django_sample .

コンテナ終了
docker-compose down

コンテナ立ち上げ
docker-compose up -d



WARNING: アカウントやパスワードはテスト用なので後で書き換える

コンテナにPostgres接続用ツールをインストール
sudo apt-get install postgresql-client

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

    Docstringに準拠したコメントをつける

    Name: 任意の名前を入力します（例: My PostgreSQL Server）。
    Connection タブ:
    Host name/address: PostgreSQL サーバーのホスト名または IP アドレスを入力します。通常は Docker Compose ファイル内で指定したコンテナ名（例: db）が使えます。
    Port: PostgreSQL のポート番号 (デフォルトは 5432)。
    Maintenance database: POSTGRES_DB で指定したデータベース名（例: mydatabase）。
    Username: POSTGRES_USER で指定したユーザー名（例: user）。
    Password: POSTGRES_PASSWORD で指定したパスワード（例: password）。
    「Save」をクリックして設定を保存します。
    ```

UUID
https://zenn.dev/kaorumori/articles/08ff8106300a7b

# 参考サイト
https://daeudaeu.com/django-staticfile/#i-4
https://daeudaeu.com/django-mechanism/#migrations
https://zenn.dev/j5ik2o/articles/a085ab3e3d0f197f6559

参考ブログ
https://itosae.com/archives/467


環境構築の参考資料
https://zv-louis.hatenablog.com/entry/2022/01/10/135321

チャット保存
https://chat.openai.com/share/441a217f-f795-4434-b0d9-c1b9276987e9