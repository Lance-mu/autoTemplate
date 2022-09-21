# _*_ coding:utf-8 _*-
# @Time：2022/9/21 22:51
# 作者：qianwulin
from conf.query_const import *
from utils.http_utils import httpPost


class TestHttp(object):
    def __init__(self, env='boe'):
        """

        :param env: 默认boe环境，线上需要手动输入
        """
        if env == "boe":
            self.header = eh_header(3167045781313534)
            self.params = ehp_bussiness_params_boe()

        elif env == "prod":
            self.header = eh_header(4248962681806317)
            self.params = ehp_bussiness_params_prod()
        else:
            raise ValueError("env输入错误，请重新输入")

    def test_case01(self):
        refresh = {'headers': {'Content-Type': 'application/json', 'x-tt-env': ''}}
        resp = httpPost(host="127.0.0.1",
                        path="test",
                        url_params=self.params,
                        body=refresh,
                        header=self.header)
        print("resp: ", resp)
        assert resp.status_code == 200
