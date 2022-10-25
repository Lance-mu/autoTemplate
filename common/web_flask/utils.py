#!/usr/bin/env python
# coding:utf-8

import hashlib
import time


def md5(m):
    return hashlib.md5(m.encode()).hexdigest()


def now_datetime():
    return time.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    print(now_datetime())




