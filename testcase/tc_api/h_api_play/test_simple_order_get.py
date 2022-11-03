# _*_ coding:utf-8 _*-
# @Time：2022/11/3 22:22
# 作者：qianwulin

import pytest
import allure

from conf.query_const import *
from utils.base import Utils
from utils.http_utils import httpPost

env = Utils.get_env()
print(f"！！！注意当前测试环境为：{env}")

if env == "boe":
    headers = eh_header(env)
    params = ehp_bussiness_params_boe()
else:
    headers = eh_header(env)
    params = ehp_bussiness_params_boe()


@pytest.mark.h_api_play
@pytest.mark.story("测试用例：查看订单信息")
def test_order_get():
    """

    :return:
    """
    refresh = {'': ''}
    resp = httpPost(host="127.0.0.1",
                    path="test",
                    url_params=params,
                    body=refresh,
                    header=headers)
    print("resp: ", resp)
    assert resp.status_code == 200
    assert resp['order']['sku']['name'] == '测试SKU名称'
    assert resp['BaseResp']['error']['code'] == 0, f"编码断言错误的返回：{resp}"





