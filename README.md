# django_sample
djangoの練習

djangoの立ち上げコマンド
docker-compose run web django-admin startproject django_sample .

コンテナ終了
docker-compose down

コンテナ立ち上げ
docker-compose up -d

コンテナビルド
docker-compose up --build



DBのルートアカウント
WARNING: 通常の開発では非公開にするべきだが、テスト用なので公開する
Username (leave blank to use 'root'): root
Email address: test@test.com
Password: password
Password (again): 
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.