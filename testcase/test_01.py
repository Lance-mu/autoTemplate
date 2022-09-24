# _*_ coding:utf-8 _*-
# @Time：2022/9/21 21:31
# 作者：qianwulin

import pytest, allure
from utils.test_utils.test_case import TestHttp
from utils.base import get_env


# 获取env环境
ENV = get_env()
testhttp = TestHttp(ENV)

if ENV == "boe":
    user_id = "boe_123"
elif ENV == "prod":
    user_id = "online_123"


@pytest.mark.testcase
@allure.story("模板测试case")
def test_case01():
    res01 = testhttp.test_case01()
    assert res01 == "except", f"测试test_case01实际结果：{res01}"


if __name__ == '__main__':
    print(user_id)




