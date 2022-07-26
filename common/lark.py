# _*_ coding:utf-8 _*-
# @Time：2022/7/2 19:07
# 作者：qianwulin

import json
from date_util import DateUtil
import requests

str_date = DateUtil.get_date(1)
# 你复制的webhook地址
url = "https://open.feishu.cn/open-apis/bot/v2/hook/5c4aca99-23fe-44f1-8f69-bc9cab818921"


def basic():
    payload_message = {
        "email": "",
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": f"测试报告{str_date}测试报告",
                    "content": [
                        [
                            {"tag": "text",
                             # "un_escape": True,
                             "text": "测试计划:boe & prod 测试"}
                        ],
                        [
                            {"tag": "a",
                             "text": "任务类型:执行测试计划",
                             "href": "https://open.feishu.cn/document/home/course"}
                        ],
                        [
                            {"tag": "at",
                             "text": "<at user_id='all'>所有人</at>"}
                        ],
                        [
                            {"tag": "text",
                             "text": "总共耗时:	15 分 0 秒"}
                        ],
                        [
                            {"tag": "text",
                             "text": "执行结果:执行成功, 通过率1.69 % (12 通过, 696 失败)"}
                        ]
                    ]
                }
            }
        }

    }
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload_message))

    print(response.text)


if __name__ == '__main__':
    basic()
    # 触发来源: cronjob(CRON)
    # 开始时间: 2022 - 05 - 23 T20: 00:23
    # 结束时间: 2022 - 05 - 23T20: 12:48
