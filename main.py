import os

from bottle import Bottle,route, run,request,response,static_file
from bottle import TEMPLATE_PATH, jinja2_template as template

app=Bottle() #ボトルのインスタンス作成

# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH.append(BASE_DIR + "/views")

# python ./main.py を直接実行したときはローカルサーバーを立ち上げる
if __name__ == "__main__":
    run(app=app,host="localhost", port=8081,quiet=False, reloader=True)