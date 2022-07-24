#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/7/10 10:20 下午
"""
from common.utils import Utils

ENV = Utils.get_env()


def get_sessionId(uid):
    """
    通过手机号获得sessionid
    """
    session_id_list = [
        {"iphone": 1234444555, "verification": 1536, "uid": 11111111,
         "sessionId": "sessionid=测试session",
         "remarks": "boe永久session_boe"},
        {"iphone": 1234444555, "verification": 1536, "uid": 11111111,
         "sessionId": "sessionid=测试session",
         "remarks": "线上永久session_boe"}

    ]
    for i in session_id_list:
        if uid == i["uid"]:
            return i["sessionId"]
    else:
        return str("sessionId不存在")


def eh_header(uid):
    """

    """
    sessionId = str(get_sessionId(uid))
    eht_headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Cookie": sessionId}
    if ENV == "boe":
        eht_headers["X-Use-Boe"] = "1"
    return eht_headers


def ehp_bussiness_params_boe():
    ehp_url_params = {
        "device_id": "12345",  # "6935111024870426125"
        "device_type": "MI PLAY"
    }
    return ehp_url_params


def ehp_bussiness_params_prod():
    ehp_url_params1 = {
        "device_id": "4486440998671111",
        "device_type": "MI PLAY",
        "app_name": "ailamp",
        "user_id": "",
        "os_version": "8.1.0",
        "channel": "local_test",
        "aid": "1691",
        "version_code": "456",
        "version_name": "4.5.6",
    }
    return ehp_url_params1

class BaseTestCase:

    def get_checked_value(self, response, keyArrays, check_value=None, mark=None) -> object:
        """
        获取要被校验的对象
        """
        result = response
        currentKey = []
        for item in keyArrays:
            if type(result) != dict:
                msg = "获取到的数据不是dict, 获取数据{}失败".format(str(keyArrays))
                return {'result': None, 'msg': msg}
            currentKey.append(item)
            itemInfo = item.split('@')
            if itemInfo[0] not in result:
                msg = "从response中获取{}失败".format(str(keyArrays))
                return {'result': None, 'msg': msg}
            else:
                result = result[itemInfo[0]]
                if len(itemInfo) > 1:
                    index = eval(itemInfo[1])
                    if type(result) != list or len(result) <= index:
                        msg = "结果类型不是list或者长度不满足:{}, 目标校验参数：{}".format(str(index + 1), str(keyArrays))
                        return {'result': None, 'msg': msg}
                    result = result[index]
        return {'result': result, 'msg': str(keyArrays)}