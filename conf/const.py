#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/7/10 10:12 下午
"""
import os


def path():
    return os.path.dirname(os.path.dirname(__file__))


def join(path1, path2):
    return os.path.join(path1, path2)


PRJ_PATH = path()
API_PATH = join(PRJ_PATH, "http")
COMMON_PATH = join(PRJ_PATH, "common")
CONF_PATH = join(PRJ_PATH, "conf")
DATES_PATH = join(PRJ_PATH, "datas")


if __name__ == '__main__':
    print(CONF_PATH)

