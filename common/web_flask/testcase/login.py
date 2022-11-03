#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/6/24 4:11 下午
Author  : qianwulin@bytedance.com
"""
from flask import Flask, abort, request, render_template

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
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
            return render_template('index.html', data = data)
        else:
            # raise 主动抛出异常
            # abort函数，在网页当中抛出异常
            abort(404)
            return None


# 自定义错误处理方法
# @app.errorhandler
# def handle_404_error(err):
#     return f"出现了404错误，错误信息是{err}"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5002')
