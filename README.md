
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Welcome to your Django project on Cloud9 IDE!

Your Django project is already fully setup. Just click the "Run" button to start
the application. On first run you will be asked to create an admin user. You can
access your application from 'https://dev-nickname-dolche.c9users.io/' and the admin page from 
'https://dev-nickname-dolche.c9users.io/admin'.

## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Django docs can be found at https://www.djangoproject.com/

You may also want to follow the Django tutorial to create your first application:
https://docs.djangoproject.com/en/1.9/intro/tutorial01/

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide


####################################################################################
sugimoto added below
####################################################################################

下記のURLを参考に、RESTful apiを実装しました。
https://qiita.com/KojiOhki/items/5be98eeae72dca2260bc

【注意点】
1. サーバー起動前に一度DB migrate(db.sqlite3ファイルをDBに反映させる)必要があります
(manage.pyのある階層で)
python manage.py migrate 

2. サーバーの実行コマンド
正：cloud9のGUI上にあるRUNボタンを押す
誤：python manage.py runserver　を実行する

3.ブログ書いた人はプロジェクトを新規作成していますが、
cloud9でDjangoを開いた時にすでにプロジェクトがあったため既存のプロジェクトを流用しました。

4.その他
開発の段階では、Djangoサーバー上でhtml(のフォーム)を生成して、
そこから自サーバーに対してapiを叩くのが楽だと思います。