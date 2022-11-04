#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/10/23 6:56 下午
Author  : qianwulin@bytedance.com
"""
# https://gitee.com/yiyizhang123/python_lessons/tree/master/flask/blog_web
from flask import Flask, render_template, request, url_for, session, redirect, flash
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
    # db.session.add_all([admin, user])
    # db.session.commit()

    dic = {
        "name": "admin",
        "password": "d41d8cd98f00b204e9800998ecf8427e",
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
    if request.method == "POST":
        f = request.form
        name = f["account"]
        password = md5(f["password"])
        try:
            _type = f["type"]
        except:
            return render_template("login.html", error="用户类型为空")
        user = User.query.filter_by(name=name, role_id=int(_type)).all()
        print("user=", user, '\n', f)
        if user:
            user = user[0]
            print("type==", user.password, '\n', password)
            if user.password == password:
                session["username"] = name
                if _type == "2":
                    user_id = user.id
                    rl = Report.query.filter_by(user_id=user_id).all()
                    rlist = []
                    for r in rl:
                        rlist.append(r.__dict__)
                    return render_template("user.html", name=name, rlist=rlist)
                # 用户类型不为2，则进入管理界面
                else:
                    us = User.query.filter_by(role_id=2).all()
                    ulist = []
                    for u in us:
                        ulist.append(u.__dict__)
                    return render_template("admin.html", name=name, rlist=ulist)
            else:
                return render_template("login.html", error="密码错误")
        else:
            return render_template("login.html", error="无该用户信息")
    return render_template("login.html", error="请输入账号和密码")


@app.route("/regist", methods=["GET","POST"])
def regist():
    if request.method == "POST":
        dic = {
            "name": request.form["account"],
            "password": md5(request.form["password"]),
            "role_id": 2
        }
        avatar = request.files["avatar"]
        save_path = "./static/icon/" + avatar.filename
        avatar.save(save_path)
        dic["avator"] = save_path

        db.session.add(User(**dic))
        db.session.commit()
        session["username"] = dic["name"]
        return render_template("user.html", name=dic["name"])
    return render_template("regist.html")


@app.route("/forgetpwd")
def forgetpwd():
    if request.method == "POST":
        print("request.form",request.form)
        name = request.form["username"]
        # 管理员和用户可能同一个名字，后面待优化
        print("name=", name)
        user = User.query.filter_by(name=name).all()
        print("user=", user)
        return "test web"
    return render_template("forgetpwd.html")


# @app.route()
# def errot():


if __name__ == '__main__':

    app.run()




