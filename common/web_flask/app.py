#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/10/23 6:56 下午
Author  : qianwulin@bytedance.com
"""
# https://gitee.com/yiyizhang123/python_lessons/tree/master/flask/blog_web
from flask import Flask, render_template, request, url_for, session, redirect
from dev import DEVConfig
from models import *
from utils1 import md5, now_datetime

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object(DEVConfig)

with app.app_context():
    db.init_app(app)  # 初始化db
    db.create_all()  # 创建为创建的表


@app.route("/initdb")
def init_db():
    # admin = Role(name="管理员")
    # user = Role(name="普通用户")
    # db.session.add_all([admin,user])
    # db.session.commit()

    dic = {
        "name": "admin",
        "password": "123",
        "role_id": 1,
        "create_time": "2020-10-25 20:22",
        "avator": "https://img2.baidu.com/it/u=2467771531,3935277803&fm=11&fmt=auto&gp=0.jpg"
    }
    user = User(**dic)
    db.session.add(user)
    db.session.commit()
    return "添加成功{}".format(dic)


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        name = request.form["account"]
        password = md5(request.form["password"])
        _type = request.form["type"]
        print("====", _type)
        user = User.query.filter_by(name=name, role_id=int(_type)).all()
        if user:

            pass
        else:
            return render_template("login.html", error="无该用户信息")
        user = user[0]
        if user.password != password:
            return render_template("login.html", error="用户密码错误")
        if _type == "2":
            session["username"] = name
            user_id = user.id
            rl = Report.query.filter_by(user_id=user_id).all()
            rlist = []
            for r in rl:
                rlist.append(r.__dict__)
            return render_template("user.html", name=name, rlist=rlist)
        else:
            session["username"] = name
            us = User.query.filter_by(role_id=2).all()
            ulist = []
            for u in us:
                ulist.append(u.__dict__)
            return render_template("admin.html", ulist=ulist)
    return render_template("login.html", error="None")


if __name__ == '__main__':
    app.run()
    rl = Report.query.filter_by(user_id=1).all()
    print(rl)
