#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/7/19 1:20 下午
Author  : qianwulin@bytedance.com
"""
import pymysql


def execute_sql(sql):
    db = pymysql.connect(
        host = " ",
        user = " ",
        password = " ",
        db = " "
    )
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
    except Exception as error:
        raise ValueError(f"请检查数据库执行语句：{error}")
    cursor.close()
    db.close()
    return data


if __name__ == '__main__':
    execute_sql("select * from user where user_id=1")
