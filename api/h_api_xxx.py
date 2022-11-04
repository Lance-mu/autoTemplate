#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/7/10 10:27 下午
Author  : qianwulin@bytedance.com
"""
import os, sys
from utils.http_utils import HttpPost

hapi = HttpPost()

class HApiXxx:

    def h_cloud_xxx(self):
        """
        form_data: 表单数据
        refresh_data: 结构体中需要更新的数据, dict类型
        """
        file_name = os.path.basename(__file__)  # 获取当前py文件名称
        method_name = sys._getframe().f_code.co_name  # 获取当前func名称

        env = Utils.get_env()
        psm = file_name.replace(".py", "")
        domain = Utils.get_conf("domains", f"{env}_{psm}_domain")  # 从conf/conf.ini中获取请求domain

        data, headers = JsonParse().get_req_json(file_name, method_name, refresh=refresh_data)  # 获取更新后的请求结构体
        body_param = data.get("body_param", None)
        query_param = data.get("query_param", None)
        files = data.get("files", None)
        form_data = data.get("form_data", None)

        url = domain + "/h_cloud/play/hello"
        hc = HTTPClient()
        return hc.post(url=url, form_data=form_data, json_data=body_param, params=query_param, files=files,
                       headers=headers)


apixxx = HApiXxx()
