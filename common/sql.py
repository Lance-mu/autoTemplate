#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/7/19 1:20 下午
Author  : qianwulin@bytedance.com
"""
import pymysql
from common.utils import Utils


class Sql:
    def __init__(self, **kwargs):
        """
        连接数据库，返回成功或失败原因
        :param kwargs: 后续用于扩展默认外的数据库
        """
        self.host = Utils().get_conf("sql", "host")
        self.user = Utils().get_conf("sql", "user")
        self.password = Utils().get_conf("sql", "password")
        self.db = Utils().get_conf("sql", "db")
        try:
            self.db = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                      db=self.db)
        except Exception as e:
            print('连接数据失败【' + str(e) + '】')

    def close(self):
        self.db.close()

    def execute_sql(self, sql):
        """
        :param sql: 需要执行的SQL语句
        :return:
        """
        res = sql.split(" ")[0]
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            if 'select' in res.lower():
                des = cursor.description[0]
                result = dict(zip(des, data))  # 将返回数据格式化成JSON串
            elif 'insert' in res.lower() or 'update' in res.lower():
                self.db.commit()  # 提交数据操作，不然插入或者更新，数据只会更新在缓存，没正式落库
                result = ''
        except Exception as error:
            raise ValueError(f"请检查数据库执行语句：[{error}]")
        cursor.close()
        self.close()
        return result


if __name__ == '__main__':
    py_sql = Sql()
    py_sql.execute_sql("select * from user")

