#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/7/13 1:06 下午
Author  : qianwulin@bytedance.com
"""

import pytest
# from tools.yamler import Yamler
# from webapi_keyword_server import WebApiKeyWordServer


# @pytest.fixture(scope='session', autouse=True, name="huadong_marketing_saler")
# def get_token_for_crm_huadong_marketing_saler() -> dict:
#     yamler = Yamler()
#     webapi_keyword_server = WebApiKeyWordServer()
#     _list_for_crm_user_token = ["conftest", "User_Token", "CRM", "HuaDong", "marketing", "saler"]
#     all_crm_user_token = yamler.from_yaml_get_configs(whichItems=_list_for_crm_user_token)
#
#     function_name = all_crm_user_token["method"]
#     del all_crm_user_token["method"]
#     key_path = all_crm_user_token["key_path"]
#     del all_crm_user_token["key_path"]
#
#     result = getattr(webapi_keyword_server, function_name)(**all_crm_user_token)
#     _token = webapi_keyword_server.webapi_get_text(_dict=result.text, keyword=key_path)
#
#     return _token[0]
#
#
# @pytest.fixture(scope='session', autouse=True, name="jiahe_marketing_saler")
# def get_token_for_crm_jiahe_marketing_saler() -> dict:
#     yamler = Yamler()
#     webapi_keyword_server = WebApiKeyWordServer()
#     _list_for_crm_user_token = ["conftest", "User_Token", "CRM", "JiaHe", "marketing", "saler"]
#     all_crm_user_token = yamler.from_yaml_get_configs(whichItems=_list_for_crm_user_token)
#
#     function_name = all_crm_user_token["method"]
#     del all_crm_user_token["method"]
#     key_path = all_crm_user_token["key_path"]
#     del all_crm_user_token["key_path"]
#
#     result = getattr(webapi_keyword_server, function_name)(**all_crm_user_token)
#     _token = webapi_keyword_server.webapi_get_text(_dict=result.text, keyword=key_path)
#
#     return _token[0]


if __name__ == '__main__':
    # crm_huadong_marketing_saler_token = get_token_for_crm_huadong_marketing_saler()
    # print(crm_huadong_marketing_saler_token)
    # crm_jiahe_marketing_saler_token = get_token_for_crm_jiahe_marketing_saler()
    # print(crm_jiahe_marketing_saler_token)
    pass