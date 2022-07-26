#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/7/11 2:49 下午
Author  : qianwulin@bytedance.com
"""
import time
import datetime


class DateUtil(object):

    @classmethod
    def get_today(cls) -> (int, int):
        '''
        获取今日0点和今日24点的时间戳
        :return:
        '''
        begin_time = datetime.date.today()
        end_time = begin_time + datetime.timedelta(days=1)
        begin_time_stamp = int(time.mktime(time.strptime(str(begin_time), '%Y-%m-%d')))
        end_time_stamp = int(time.mktime(time.strptime(str(end_time), '%Y-%m-%d'))) - 1
        return begin_time_stamp, end_time_stamp

    @classmethod
    def get_theweek(cls) -> (int, int):
        '''
        获取本周周始0点和周末24点的时间戳
        :return:
        '''
        today = datetime.date.today()
        week = today.weekday()
        begin_time = today - datetime.timedelta(days=week)
        begin_time_stamp = int(time.mktime(time.strptime(str(begin_time), '%Y-%m-%d')))
        end_time = begin_time + datetime.timedelta(days=5)
        end_time_stamp = int(time.mktime(time.strptime(str(end_time), '%Y-%m-%d'))) - 1
        return begin_time_stamp, end_time_stamp

    @classmethod
    def get_themonth(cls) -> (int, int):
        '''
        获取本月月始0点和月末24点的时间戳
        :return:
        '''
        today = datetime.date.today()
        days = today.day - 1
        begin_time = today - datetime.timedelta(days=days)
        begin_time_stamp = int(time.mktime(time.strptime(str(begin_time), '%Y-%m-%d')))
        end_time = today + datetime.timedelta(days=1)
        end_time_stamp = int(time.mktime(time.strptime(str(end_time), '%Y-%m-%d'))) - 1
        return begin_time_stamp, end_time_stamp

    @classmethod
    def get_now_timestamp(cls) -> int:
        '''
        获取当前时间点的时间戳
        :return:
        '''
        millis = int(round(time.time() * 1000))
        return millis

    @classmethod
    def get_day_timestamp(cls, days: int) -> int:
        """
        获取days后的时间戳
        :return:
        """
        now = datetime.datetime.now()
        date1 = now + datetime.timedelta(days=days)

        date = date1.strftime("%Y-%m-%d") + " 00:00:00"
        timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        date_time = int(time.mktime(timeArray) * 1000)
        return date_time

    @classmethod
    def get_date(cls, timestamp: int) -> str:
        """
        时间戳转化为年月日时间格式
        :param timestamp:
        :return:
        """
        if timestamp == 1:
            timestamp = time.time()
        timeArray = time.localtime(timestamp)
        date = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return date


if __name__ == '__main__':
    print(DateUtil.get_now_timestamp())
    print(DateUtil.get_date(1)[:10])

