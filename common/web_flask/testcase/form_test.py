#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/6/24 3:21 下午
Author  : qianwulin@bytedance.com
"""
from flask import Flask, render_template, request
from wtforms import StringField, PasswordField, SubmitField # 类型
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo # 验证数据不能为空 验证数据是否相同

app = Flask(__name__)


# 定义表单模型
class Register(FlaskForm):
    user_name = StringField(label="用户名", validators=[DataRequired("用户名不能为空")])
    password = PasswordField(label="密码", validators=[DataRequired("密码不能为空")])
    password2 = PasswordField(label="密码", validators=[DataRequired("密码不能为空"), EqualTo("password")])
    submit = SubmitField()


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        print("name:", name, "password:", password)
        return "this is post"


# 重定向的两种方法：1、到新的链接  2、到内部方法
from flask import redirect


@app.route('/indet1')
def hello1():
    return redirect("https://www.baidu.com/")


from flask import url_for


@app.route('/indet2')
def hello2():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5050')
