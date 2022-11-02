#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/10/23 6:56 下午
Author  : qianwulin@bytedance.com
"""
# https://gitee.com/yiyizhang123/python_lessons/tree/master/flask/blog_web
from flask import Flask, render_template
from dev import DEVConfig
from models import *

app = Flask(__name__, template_folder="templates",static_folder="static")
app.config.from_object(DEVConfig)

with app.app_context():
    db.init_app(app)#初始化db
    db.create_all()#创建为创建的表


@app.route("initdb")
def init_db():
    admin = Role(name="管理员")
    user = Role(name="普通用户")
    db.session.add_all([admin,user])
    db.session.commit()


if __name__ == '__main__':
    app.run()

