#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/8/5 11:45 下午
Author  : qianwulin@bytedance.com
"""
from flask import Flask, render_template, abort, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    data = {
        "status": "login success"
    }
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        if name == "zhangsan" and password == "123":
            return render_template('login.html', data=data)
        else:
            # raise 主动抛出异常
            # abort函数，在网页当中抛出异常
            abort(404)
            return None


if __name__ == '__main__':
    app.run()
