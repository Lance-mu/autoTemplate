#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/7/19 1:05 下午
Author  : qianwulin@bytedance.com
"""
import xlrd
import os
import pandas as pd
from conf.const import DATES_PATH,join

config_path = "../conf/"
api_path = "../api/"
case_path = "../testcase/tc_api/business_platform/"
api_info = join(DATES_PATH, "data/api_info.xlsx")
api_datas = pd.read_excel(api_info)

print(api_datas.sheetnames)


def write_conf_class(workbook, from_row=None, sheet_names=None):
    """
    生成配置
    :param sheet_names:  workbook.sheet_names()[1:] 接口在的sheet页
    :param workbook: 文件
    :param from_row: 从第几行开始操作,默认是从第2行
    :return:
    """
    if sheet_names is None:
        sheet_names = workbook.sheet_names()[1:]
    for sheet_name in sheet_names:
        # 如果不存在创建文件
        api_name = sheet_name.split(".")[-1]
        conf_file_name = config_path + api_name + "_conf.py"
        is_exists = os.path.exists(conf_file_name)
        sheet = workbook.sheet_by_name(sheet_name)
        file = open(conf_file_name, 'a')
        if is_exists is False:
            file.write("\n# header")
            file.write("\n" + api_name.upper() + "_HEADER = {}")
            url = sheet.cell(0, 0).value
            file.write("\n# url")
            file.write("\n" + api_name.upper() + "_URL = '" + url + "'")
        if from_row is None or from_row < 2:
            from_row = 2
        for i in range(from_row, sheet.nrows):
            # 接口类型
            request_type = sheet.cell(i, 2).value
            # 接口
            request_path = sheet.cell(i, 3).value.strip()
            # 用途
            request_use = sheet.cell(i, 1).value
            request_name = '_'.join(request_path.upper().split("/")[-2:]).strip() + "_PATH"
            file.write("\n#" + str(request_use) + "\n")
            file.write(request_name + " = ('" + request_type + "' , '" + request_path + "')\n")


def write_api_class(workbook, from_row=None, sheet_names=None):
    """
    生成api接口请求函数
    :param sheet_names:  workbook.sheet_names()[1:] 接口在的sheet页
    :param workbook: 文件
    :param from_row: 从第几行开始操作,默认是从第2行
    :return:
    """
    if sheet_names is None:
        sheet_names = workbook.sheet_names()[1:]
    for sheet_name in sheet_names:
        api_name = sheet_name.split(".")[-1]
        api_file_name = api_path + api_name + "_api"
        if os.path.exists(api_file_name) is False:
            os.makedirs(api_file_name)
            open(api_file_name + '/__init__.py', 'a')
        api_py_file_name = api_file_name + "/" + api_name + "_api" + ".py"
        is_exists = os.path.exists(api_py_file_name)
        file = open(api_py_file_name, 'a')
        if is_exists is False:
            file.write("from conf." + api_name + "_conf import *\n")
            file.write("from utils.http_new_utils import do_query\n\n\n")
        sheet = workbook.sheet_by_name(sheet_name)
        if from_row is None or from_row < 2:
            from_row = 2
        for i in range(from_row, sheet.nrows):
            # 接口类型
            request_type = sheet.cell(i, 2).value
            # 接口
            request_path = sheet.cell(i, 3).value
            # 用途
            request_use = sheet.cell(i, 1).value
            request_name = '_'.join(request_path.split("/")[-2:])
            if sheet_name == "h.api.play":
                file.write("def " + request_name + "(req, parent=None, check_schema=None, client=False):\n")
            else:
                file.write("def " + request_name + "(req, header=None, check_schema=None, client=False):\n")
            file.write("    \"\"\"\n")
            file.write("    " + request_use + "接口请求\n")
            file.write("    :param req:请求参数\n")
            file.write("    :param check_schema:返回schema校验，默认为不校验\n")
            file.write("    :param client:端内/端外标识\n")
            file.write("    :return:\n")
            file.write("    \"\"\"\n")
            file.write("if client:\n        header = " + api_name.upper() + "[1]\n        host = " + api_name.upper() +
                       "[1]\n    else:\n        header = " + api_name.upper() + "[0]\n        host = " + api_name.upper() + "[0]\n")
            request_path_name = '_'.join(request_path.upper().split("/")[-2:]).strip() + "_PATH"
            if request_type == "GET":
                file.write(
                    "    " + "resp = do_query(host=host, request_type_path=" + request_path_name+ ", url_params=req, header=header, normal_check=False, check_schema=check_schema)\n")
            else:
                if sheet_name == "h.api.play":
                    file.write(
                        "    " + "resp = do_query(host=host, request_type_path=" + request_path_name + ", body=req, url_params=URL_PARAMS, header=header, normal_check=False, check_schema=check_schema)\n")
                else:
                    file.write(
                        "    " + "resp = do_query(host=host, request_type_path=" + request_path_name + ", body=req, header=header, normal_check=False, check_schema=check_schema)\n")
            file.write("    return resp\n\n\n")


def write_case_class(workbook, from_row=None, sheet_names=None):
    """
    生成case层
    :param sheet_names:  workbook.sheet_names()[1:] 接口在的sheet页
    :param workbook: 文件
    :param from_row: 从第几行开始操作,默认是从第2行
    :return:
    """
    if sheet_names is None:
        sheet_names = workbook.sheet_names()[1:]
    for sheet_name in sheet_names:
        api_name = sheet_name.split(".")[-1]
        api_file_name = case_path + api_name + "_api"
        if os.path.exists(api_file_name) is False:
            os.makedirs(api_file_name)
            open(api_file_name + '/__init__.py', 'a')
        sheet = workbook.sheet_by_name(sheet_name)
        if from_row is None or from_row < 2:
            from_row = 2
        for i in range(from_row, sheet.nrows):
            request_path = sheet.cell(i, 3).value.strip()
            # 用途
            request_use = sheet.cell(i, 1).value.strip()
            api_file_sub_name = api_file_name + "/"
            if os.path.exists(api_file_sub_name) is False:
                os.makedirs(api_file_sub_name)
                open(api_file_sub_name + '/__init__.py', 'a')
            request_path_title = ''.join(request_path.title().split("/")[-2:]).replace("_", "")
            case_py_file_name = api_file_sub_name + request_path_title[
                0].lower() + request_path_title[1:] + "_test.py"
            date_py_file_name = api_file_sub_name + request_path_title[
                0].lower() + request_path_title[1:] + "_data.py"
            case_file = open(case_py_file_name, 'a')
            case_file.write("import pytest\n")
            case_file.write("import allure\n\n\n")
            case_file.write("from api." + api_name + "_api import " + api_name + "_api\n")
            date_py_file_name.replace("/", ".")
            data_key = '_'.join(request_path.split("/")[-2:]) + "_normal_data"
            case_file.write(
                "from " + date_py_file_name.replace("/", ".")[3:-3] + " import " + data_key + "\n")
            case_file.write("from utils import assert_base\n")
            case_file.write("from utils.log_utils import Log\n")
            case_file.write("from utils.params_util import runtime\n\n\n")
            case_file.write("@pytest.mark.smoke\n")
            case_file.write("@pytest.mark.boe\n")
            case_file.write("@pytest.mark." + get_mark(sheet_name=sheet_name) + "\n")
            case_file.write("@runtime(data=" + data_key + ")\n")
            case_file.write("@allure.title(\"" + request_use + "\")\n")
            case_key = "test_" + '_'.join(request_path.split("/")[-2:]) + "_normal"
            case_file.write("def " + case_key + "(title, params, expected):\n")
            case_file.write("\t\"\"\"\n")
            case_file.write("\t接口" + request_path + "\n")
            case_file.write("\t\"\"\"\n")
            case_file.write("\tLog.info(\"开始运行case:{}\".format(title))\n")
            case_file.write("\twith allure.step(\"1.请求接口：\"):\n")
            request_name = '_'.join(request_path.split("/")[-2:])
            case_file.write("\t\tresp = " + api_name + "_api." + request_name + "(req=params)\n")
            case_file.write("\twith allure.step(\"2.校验返回：\"):\n")
            case_file.write("\t\tassert_base.generate_assert(data=resp, expected=expected)\n")
            data_file = open(date_py_file_name, 'a')
            data_file.write(data_key + "=[\n")
            data_file.write("\t{\n")
            data_file.write("\t\t\"title\": \"" + request_use + "\",\n")
            data_file.write("\t\t\"params\": {},\n")
            data_file.write("\t\t\"expected\": {},\n")
            data_file.write("\t}\n")
            data_file.write("]\n")


def get_mark(sheet_name):
    if sheet_name == "h.api.play":
        return "play"
    else:
        return ""

class SimpleApi:
    def __init__(self):
        pass

    def write_conf_class(self):
        pass


if __name__ == '__main__':
    """
        适用于新接口，第一次加case
        1、将接口写入文件「服务列表.xls」中,不需要的接口清除一下
        2、文档样式不要动
        3、想要生成什么就调什么接口
        4、如果文件已经存在，就是在原文件里续写
        5、参数
            . sheet_names,比如接口在第2页，sheet_names=workbook.sheet_names()[2:3]
            . from_row,比如新增接口在第4行开始,from_row=3
        6、或者将不写的接口都删了
        """
    # workbook = xlrd.open_workbook('服务列表.xls')
    # write_conf_class(workbook)
    # write_api_class(workbook)
    # write_case_class(workbook)
    pass

