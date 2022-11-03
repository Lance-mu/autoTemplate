#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/7/10 10:23 下午
Author  : qianwulin@bytedance.com
"""
from configparser import ConfigParser
import os


class Utils(object):
    @staticmethod
    def get_conf(section, key):
        '''
        框架中底层所使用的方法，业务可以使用，用于读取指定conf文件下的key，使用方法：Utils().get_conf(section='boe', key='header')
        :param section: section区域
        :param key: key值
        :return:
        '''
        file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "conf", f"conf.ini")
        config = ConfigParser()
        config.read(file)
        try:
            return config[section][key]
        except KeyError:
            raise KeyError(f"conf.ini, section:{section},key:{key} not found, please check!")

    @staticmethod
    def get_header_conf(section):
        '''
        用于读取指定conf文件下的key，使用方法：Utils().get_header_conf(section='boe')
        :param section: section区域
        :return: dict
        '''
        file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "conf", f"conf.ini")
        config = ConfigParser()
        config.read(file)
        return dict(config._sections)[section]

    @staticmethod
    def get_env():
        '''
        用于获取当前的env环境，使用方法:Utils().get_env()
        :return:
        '''
        if os.getenv("atlas_cluster"):
            return os.getenv("atlas_cluster")
        else:
            return Utils.get_conf("common", "env")

    @staticmethod
    def get_env_label():
        '''
        用于获取当前的env_label标签，使用方法:Utils().get_env_label()
        :return:
        '''
        if os.getenv("ENV_LABEL"):
            return os.getenv("ENV_LABEL")
        else:
            try:
                return Utils.get_conf("common", "env_label")
            except KeyError:
                return None


def requ_info():
    """
    根据配置信息，直接返回对应header和body参数
    :return:
    """
    pass


allfiles = []

# 递归
def getAllFiles(path, level):
    childFiles = os.listdir(path)
    for file in childFiles:
        filepath = os.path.join(path,file)
        if os.path.isdir(filepath):
            getAllFiles(filepath, level+1)
        allfiles.append("\t"*level + filepath)

if __name__ == '__main__':
    """
    env是测试环境，env_label环境变量，ini文件不兼容时，去除注释
    """
    # print(Utils.get_env())
    getAllFiles("web_flask", 0)
    for i in allfiles:
        print(i)