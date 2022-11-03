#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/6/25 11:39 上午
Author  : qianwulin@bytedance.com
# 一个网站，可以添加和删除
"""
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import os

app = Flask(__name__)
# 数据库配置：数据库地址/关闭自动跟踪修改
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root1234@127.0.0.1:3306/web_flask?charset=utf8mb4"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config['SECRET_KEY'] ='AASDFASDF'
import config
app.config.from_object(config)

"""
1、配置数据库
2、添加书和作者模型
3、添加数据
4、使用模版显示数据库查询的数据

"""
db = SQLAlchemy(app)


class Author(db.Model):
    # 表名
    __tablename__ = "authors"
    # 字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    # 关系引用
    # books是给自己（Author模型）用的，author是给Book模型用的
    books = db.relationship('Book', backref='author')

    def __repr__(self):
        return f"Author:{self.name}"


# 书籍模型
class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))

    def __repr__(self):
        return f"Book:%s: %s" % (self.name, self.author_id)


# 自定义表单类
class AuthorForm(FlaskForm):
    author = StringField("作者", validators=[DataRequired()])
    book = StringField("书籍", validators=[DataRequired()])
    submit = SubmitField("提交")


# 删除书籍
@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    book = Book.query.get(book_id)

    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            print(e)
            flash("删除书籍出错")
            db.session.rollback()
    else:
        flash("书籍找不到")
    return redirect(url_for('index'))


@app.route("/delete/author/<author_id>")
def delete_author(author_id):
    author = Author.query.get(author_id)

    if author:
        try:
            # 查询之后直接删除
            Book.query.filter_by(author_id=author_id).delete()
            # 删除作者
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            print(e)
            flash("删除作者出错")
            db.session.rollback()
    else:
        flash("作者找不到")
    return redirect(url_for('index'))


# 添加书籍
@app.route("/", methods=['GET', 'POST'])
def index():
    author_form = AuthorForm()

    # 验证逻辑，实现验证
    if author_form.validate_on_submit():
        author_name = author_form.author.data
        book_name = author_form.book.data

        author = Author.query.filter_by(name=author_name).first()
        if author:
            book = Book.query.filter_by(name=book_name).first()
            if book:
                flash("已存在同名书籍")
            else:
                try:
                    new_book = Book(name=book_name, author_id=author.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash("添加书籍失败")
                    db.session.rollback()

        else:
            try:
                new_author = Author(name=author_name)
                db.session.add(new_author)
                db.session.commit()

                new_book = Book(name=book_name, author_id=new_author.id)
                db.session.add(new_book)
                db.session.commit()
            except Exception as e:
                print(e)
                flash("添加作者和书籍失败")
                db.session.rollback()

    else:
        if request.method == "POST":
            flash("参数不全")

    authors = Author.query.all()
    return render_template("books.html", authors=authors, form=author_form)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    # 生成数据
    au1 = Author(name="作者1")
    au2 = Author(name="作者2")
    au3 = Author(name="作者3")

    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()

    bk1 = Book(name="书籍1", author_id=au1.id)
    bk2 = Book(name="书籍2", author_id=au1.id)
    bk3 = Book(name="书籍3", author_id=au2.id)
    bk4 = Book(name="书籍4", author_id=au3.id)
    bk5 = Book(name="书籍5", author_id=au3.id)

    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    db.session.commit()

    app.run(port="5051")
