#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/7/10 10:39 下午
Author  : qianwulin@bytedance.com
"""
import logging
import time
import os
from logging import handlers
from logging.handlers import TimedRotatingFileHandler


class Log:
    def __init__(self):
        logFilePath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/output/" + \
                      time.strftime("%Y_%m_%d") + ".log"
        fmt = "%(asctime)s - %(pathname)s - %(levelname)s %(lineno)d行: %(message)s"
        self.logger = logging.getLogger()  # 创建日志器
        self.logger.setLevel(logging.INFO)  # 设置级别
        self.logger = logging.getLogger(logFilePath)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        #
        th = handlers.TimedRotatingFileHandler(
            filename=logFilePath,
            when='D',
            backupCount=3,
            encoding='utf-8')
        """
            往文件里写入#指定间隔时间自动生成文件的处理器
            实例化TimedRotatingFileHandler
            interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
            S 秒
            M 分
            H 小时、
            D 天、
            W 每星期（interval==0时代表星期一）
            midnight 每天凌晨
        """
        th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(th)

        print(logFilePath)


log = Log().logger


