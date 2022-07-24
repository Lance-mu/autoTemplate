#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/7/9 9:19 下午
"""
import os
import xlrd
# from conf.rpc_constant_conf import *

config_path = "../conf/"
rpc_path = "../rpc/"
case_path = "../testcase/tc_rpc/"  # 生成test_case的路径


def write_test_file(file_name, name, method, test_method_name, desc):
    psm_name = name.replace('.', '_')
    rpc_file_name = "rpc." + psm_name
    test_file_name = case_path + get_mark(name) + '_rpc/' + file_name + '_test.py'
    data_file_name = case_path + get_mark(name) + '_rpc/' + file_name + '_data.py'
    dirs = case_path + get_mark(name) + '_rpc/'
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    if not os.path.exists(test_file_name):
        os.system(r"touch {}".format(test_file_name))
    test_file = open(test_file_name, 'a+')
    test_file.write('import allure\n')
    test_file.write('import pytest\n')
    test_file.write('from ' + rpc_file_name + ' import ' + method + '\n')
    data_key = test_method_name + "_normal_data"
    test_file.write(
        "from " + data_file_name.replace("/", ".")[3:-3] + " import " + data_key + "\n")
    test_file.write("from utils import assert_base\n")
    test_file.write("from utils.log_utils import Log\n")
    test_file.write("from utils.params_util import runtime\n\n\n")
    test_file.write("@pytest.mark.smoke\n")
    test_file.write("@pytest.mark.boe\n")
    test_file.write("@pytest.mark." + get_mark(name) + "\n")
    test_file.write("@runtime(data=" + data_key + ")\n")
    test_file.write("@allure.title(\"" + desc + "\")\n")
    test_func_name = 'def test_%s(title, params, expected):' % test_method_name
    test_file.write(test_func_name + "\n")
    test_file.write("\t\"\"\"\n")
    test_file.write("\trpc方法:" + method + "\n")
    test_file.write('\t"""\n')
    test_file.write("\tLog.info(\"开始运行case:{}\".format(title))\n")
    test_file.write('\twith allure.step("step1 请求接口: %s"):\n' % desc)
    test_file.write("\t\tresp = " + method + "(req=params)\n")
    test_file.write("\twith allure.step(\"2.校验返回：\"):\n")
    test_file.write("\t\tassert_base.assert_rpc_base_data(resp=resp, expected=expected)\n")
    data_file = open(data_file_name, 'a')
    data_file.write(data_key + " = [\n")
    data_file.write("\t{\n")
    data_file.write("\t\t\"title\": \"" + desc + "\",\n")
    data_file.write("\t\t\"params\": {},\n")
    data_file.write("\t\t\"expected\": {},\n")
    data_file.write("\t}\n")
    data_file.write("]\n")


def get_mark(name):
    if name == "h.svr.play_trade":
        return "play_trade"
    if name == "h.svr.play_market":
        return "play_market"
    if name == "h.svr.play_order":
        return "play_order"
    if name == "h.svr.play_store":
        return "play_store"
    if name == "h.svr.bank":
        return "bank"
    else:
        return ""


def write_conf_file(psm, svc, idl):
    write_conf = open('../conf/rpc_constant_conf.py', 'a')
    psm_name = psm.title().replace(".", "_") + "_PSM"
    svc_name = psm.title().replace(".", "_") + "_SVC"
    idl_name = psm.title().replace(".", "_") + "_IDL"
    write_conf.write(psm_name + " = \"" + psm + "\"\n")
    write_conf.write(svc_name + " = \"" + svc + "\"\n")
    write_conf.write(idl_name + " = \"" + idl + "\"\n\n")


def write_rpc_file(psm, method, request_use):
    rpc_file_name = "../rpc/" + psm.replace('.', '_') + '.py'
    if not os.path.exists(rpc_path):
        os.makedirs(rpc_path)
    if not os.path.exists(rpc_file_name):
        os.system(r"touch {}".format(rpc_file_name))
        with open(rpc_file_name, 'a+') as file:
            file.write('from conf.rpc_constant_conf import *\n')
            file.write('from utils import rpc_utils\n\n')
    with open(rpc_file_name, 'a+') as file:
        request_use = request_use
        file.write("\ndef %s(req):\n" % method)
        file.write("    \"\"\"\n")
        file.write("    " + request_use + "rpc请求\n")
        file.write("    :param req:请求参数\n")
        file.write("    :return:\n")
        file.write("    \"\"\"\n")
        file.write('    resp = rpc_utils.request(psm=%s, svc=%s, idl=%s, method="%s", req=%s)\n' % (
            psm.title().replace(".", "_") + '_PSM', psm.title().replace(".", "_") + '_SVC',
            psm.title().replace(".", "_") + '_IDL',
            method, 'req'))
        file.write("    return resp\n")


def get_method_name(text):
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)
    return "".join(lst).lower()


if __name__ == '__main__':
    workbook = xlrd.open_workbook('rpc服务列表.xls')
    sheet_names = workbook.sheet_names()[1:]
    for sheet_name in sheet_names:
        sheet = workbook.sheet_by_name(sheet_name)
        # svc
        svc = sheet.cell(0, 0).value.strip()
        # idl
        idl = sheet.cell(1, 0).value.strip()
        from_row = 4  # 从第4行开始读方法，此处可更改
        write_conf_file(sheet_name, svc, idl)  # 1.write_conf_file
        for i in range(from_row, sheet.nrows):
            # 接口说明
            rpc_info = sheet.cell(i, 0).value.strip()
            # 接口
            method = sheet.cell(i, 2).value.strip()
            file_name = method[:1].lower() + method[1:]
            write_rpc_file(sheet_name, method, rpc_info)  # 2.write_rpc_file
            test_method_name = get_method_name(method)
            write_test_file(file_name, sheet_name, method, test_method_name, rpc_info)  # 3.write_case_file


