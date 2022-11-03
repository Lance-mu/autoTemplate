#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/8/5 11:45 下午
Author  : qianwulin@bytedance.com
"""
from flask import Flask, render_template, abort, request, url_for

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('login/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # 取表单参数
        f = request.form
        name = f["username"]
        password = f["password"]
        if name == "admin" and password == "123456":
            return render_template('home.html', name=name)
        # raise 主动抛出异常、abort函数，在网页当中抛出异常
        # abort(404)
        return "账号或者密码错误"
    elif request.method == "GET":
        # 取链接参数
        name = request.args['name']
        pwd = request.args.get("pwd", "123456")
        return "姓名{0}密码{1}".format(name, pwd)
    else:
        return "请求方式不正确"


if __name__ == '__main__':
    app.run(host="192.168.132.1", port=808)
