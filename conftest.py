#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/7/10 10:33 下午
Author  : qianwulin@bytedance.com
"""
import pytest
import time


@pytest.fixture(scope="function", params=None, autouse=False, ids=None, name=None)
def wati_time():
    """
    scope: 用于控制Fixture的作用范围,作用类似于Pytest的setup/teardown
    params: Fixture的可选形参列表，支持列表传入 默认None
    autouse: 默认False.若为True，刚每个测试函数都会自动调用该fixture,无需传入fixture函数名
    ids: 用例标识ID 与params配合使用，一对一关系
    name: 通常来说使用 fixture 的测试函数会将 fixture 的函数名作为参数传递，如果使用了name,那只能将name传如，函数名不再生效

    针对订单创建有幂等验证，可以设置间隔时间
    :return:
    """
    # 前置条件
    time.sleep(0.5)
    yield
    # 后置条件
