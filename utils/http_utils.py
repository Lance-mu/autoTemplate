#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/7/10 10:35 下午
Author  : qianwulin@bytedance.com
"""

import requests
from urllib.parse import urlencode
import json
import os
import urllib3
from json import loads, dumps
from urllib import parse
from requests import post, get
from conf.http_const import RequestType
from common.log import Log
from jsonschema import validate, draft7_format_checker
from jsonschema.exceptions import SchemaError, ValidationError

urllib3.disable_warnings()


class httpGet():
    def __init__(self, host, path, url_params, header):
        self.url = "{}{}?{}".format(host, path, urlencode(url_params))
        self.header = header

    # @retry(tries=5, delay=3)
    def doRequest(self):
        resp = requests.get(url=self.url, headers=self.header)
        assert resp.status_code == 200, f"get返回非200，内容：{resp}"
        return resp


class httpPost():
    def __init__(self, host, path, url_params, body, header):
        self.url = "{}{}?{}".format(host, path, urlencode(url_params))
        self.body = body
        self.header = header

    def doRequest(self):
        resp = requests.post(url=self.url, data=self.body, headers=self.header)
        assert resp.status_code == 200, f"post返回非200，内容：{resp}"
        return resp



def do_query(host, request_type_path, body=None, url_params=None, header=None,
             not_json=False, normal_check=True,
             check_schema=None):
    """
    接口请求
    :param request_type_path: request_type & 接口路径 eg:('POST' or 'GET', 'path')，与path和request_type参数互斥，只能传一种。
    # :param request_type: 支持GET、POST
    :param host: 域名
    # :param path: 接口
    :param body: POST请求body
    :param url_params: 接口参数
    :param header: header
    :param not_json: 返回是否不是json,默认是
    :param normal_check: 是否进行基础校验，默认校验
    :param check_schema: 进行schema校验，默认不校验，传schema进行校验
    :return:
    """
    resp = None
    host_path = host + request_type_path[1]
    request_type = RequestType(str(request_type_path[0]).upper())
    try:
        if request_type == RequestType.GET:
            hc = Client(headers=header)
            hc.url = host_path
            hc.params = url_params
            resp = hc.get()
        if request_type == RequestType.POST:
            hc = Client(headers=header)
            hc.url = host_path
            hc.params = url_params
            hc.body = body
            resp = hc.post()
        if request_type == RequestType.POST_FORM_DATA:
            hc = Client(headers=header)
            hc.url = host_path
            hc.params = url_params
            hc.body = body
            resp = hc.post()
    except Exception as e:
        Log.error("请求出错Err:{}".format(e))
        resp = None

    return check_resp(resp, not_json, normal_check, check_schema)


def check_resp(resp, not_json, normal_check, check_schema):
    # 默认校验reponse内容是否为None
    assert resp is not None

    if not not_json:
        resp_json = resp.json()
        Log.info("美化response\n{}".format(json.dumps(resp_json, sort_keys=True, indent=4, ensure_ascii=False)))

        if check_schema is not None:
            assert check_json_schema(resp_json, check_schema) == True
        if normal_check:
            # 兼容返回error={}
            assert resp_json['err_no'] == 0 or resp_json["err_tips"] == ''
        return resp_json
    else:
        return resp.text


def check_json_schema(resp, check_schema) -> bool:
    """
    json-schema校验接口
    :param resp: 待校验response
    :param check_schema: 需校验json_schema
    :return: bool
    """
    try:
        validate(instance=resp, schema=check_schema, format_checker=draft7_format_checker)
    except SchemaError as e:
        Log.error("Response校验schema出错：\n出错位置：{}\n提示信息：{}".format(" --> ".join([i for i in e.path]), e.message))
        return False
    except ValidationError as e:
        Log.error("json数据不符合schema规定：\n出错字段：{}\n提示信息：{}".format(" --> ".join([i for i in e.path]), e.message))
        return False
    else:
        return True


class Client:
    def __init__(self, url="", headers=None):
        if headers is None:
            headers = {}
        self.headers = headers
        self.url = url
        if 'Content-Type' not in headers.keys():
            self.headers['Content-Type'] = "application/json; charset=utf-8"
        # 获取临时环境标签
        if os.environ.get('ENV_LABEL', None) is not None:
            self.headers["X-USE-BOE"] = "1"
            self.headers['x-tt-env'] = os.environ.get('ENV_LABEL', None)
        self.body = {}
        self.params = {}

    def serialize(self):
        if self.headers['Content-Type'] == 'application/x-www-form-urlencoded':
            self.body = parse.urlencode(self.body)
        else:
            self.body = dumps(self.body)

    def unserialize(self, resp):
        if resp.status_code == 200:
            log_id = resp.headers.get("X-Tt-logid", None)
            Log.info(f'此次 logid {log_id}.')
            resp_dict = loads(resp.text)
            Log.info(f'返回结果 {resp_dict}.')
            return resp
        else:
            Log.info(f'返回结果 {resp.text}.')
            raise Exception({"logId": resp.headers['X-Tt-Logid']})

    def post(self):
        self.serialize()
        Log.info("本次POST请求信息为：\nurl：{0};\nheaders：{1};\nbody:{2};\nparams:{3}".format(
            self.url, self.headers, self.body, self.params))
        resp = post(self.url, headers=self.headers, data=self.body, params=self.params, verify=False)
        return self.unserialize(resp)

    def get(self):
        self.serialize()
        Log.info("本次GET请求信息为：\nurl：{0};\nheaders：{1};\nparams:{2}".format(
            self.url, self.headers, self.params))
        resp = get(self.url, params=self.params, headers=self.headers, verify=False)
        return self.unserialize(resp)


