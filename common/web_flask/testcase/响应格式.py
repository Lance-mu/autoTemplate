#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/6/24 3:53 下午
Author  : qianwulin@bytedance.com
"""
from flask import Flask,make_response,json,jsonify

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route('/')
def hello_world1():

    return "<h1>测试flask<h1>"

@app.route('/resp')
def resp():
    data = {
        "name": "张三"
    }
    # response = make_response(json.dumps(data, ensure_ascii=False))  # ensure_ascii设置格式content-type
    # response.mimetype = "application/json"
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5001')
