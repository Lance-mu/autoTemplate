#!/usr/bin/env python
# coding:utf-8

class DEVConfig(object):
    DEBUG = True
    SECRET_KEY = 'qian'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{ipaddress}:{port}/{database}?charset=utf8mb4".format(
        username="root", password="root1234", ipaddress="127.0.0.1", port=3306, database="web_flask")
    # 动态追踪修改设置
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 执行数据查询时会显示sql语句
    SQLALCHEMY_ECHO = True
