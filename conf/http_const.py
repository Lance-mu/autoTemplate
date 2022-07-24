#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/7/22 12:26 下午
Author  : qianwulin@bytedance.com
"""

from enum import Enum, unique


@unique
class RequestType(Enum):
    """
        最好每一个名字和值都是唯一
    """
    GET = 'GET'
    POST = 'POST'
    POST_FORM_DATA = 'POST-FORM-DATA'


if __name__ == '__main__':
    print(RequestType('GET'))
