#coding:utf-8

# bot とは直接関係ないけど、動作を安定させるための（？）ダミープログラム。
import os
from bottle import route, run

@route("/")
def hello_world():
        return "hello world"

run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))