import allure
import pytest
from rpc.h_svr_play_order import CreateOrder
from testcase.tc_rpc.play_order_rpc.createOrder_data import create_order_normal_data
from utils import assert_base
from utils.log_utils import Log
from utils.params_util import runtime


@pytest.mark.smoke
@pytest.mark.boe
@pytest.mark.play_order
@runtime(data=create_order_normal_data)
@allure.title("创建订单")
def test_create_order(title, params, expected):
	"""
	rpc方法: CreateOrder
	"""
	Log.info("开始运行case:{}".format(title))
	with allure.step("step1 请求接口: 创建订单"):
		resp = CreateOrder(req=params)
	with allure.step("2.校验返回："):
		assert_base.assert_rpc_base(resp)
		Log.info("新建的订单id为:{}".format(resp['orderId']))
		assert_base.assert_rpc_base_data(resp=resp, expected=expected)
