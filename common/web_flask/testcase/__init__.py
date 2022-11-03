#!/usr/bin/env python
# coding:utf-8
"""
Time    : 2022/6/27 6:20 下午
Author  : qianwulin@bytedance.com
"""


class ContentStash(object):
    """
    content stash for online operation
    pipeline is
    1. input_filter: filter some contents, no use to user
    2. insert_queue(redis or other broker): insert useful content to queue
    """

    def __init__(self):
        self.input_filter_fn = None
        self.broker = []

    def register_input_filter_hook(self, input_filter_fn):
        """
        register input filter function, parameter is content dict
        Args:
            input_filter_fn: input filter function
        Returns:
        """
        self.input_filter_fn = input_filter_fn

    def insert_queue(self, content):
        """
        insert content to queue
        Args:
            content: dict
        Returns:
        """
        self.broker.append(content)

    def input_pipeline(self, content, use=True):
        """
        pipeline of input for content stash
        Args:
            use: is use, defaul False
            content: dict
        Returns:
        """
        if not use:
            return "no use"

        # input filter
        if self.input_filter_fn:
            print("self.input_filter_fn")
            _filter = self.input_filter_fn(content)

        # insert to queue
        if not _filter:
            self.insert_queue(content)


# test
## 实现一个你所需要的钩子实现：比如如果content 包含time就过滤掉，否则插入队列
def input_filter_hook(content):
    """
    test input filter hook
    Args:
        content: dict
    Returns: None or content
    """
    if content.get('time') is None:
        return
    else:
        return content


# 原有程序
def main():

    content = {'filename': 'test.jpg', 'b64_file': "#test", 'data': {"result": "cat", "probility": 0.9}}
    content_stash = ContentStash()

    # 挂上钩子函数， 可以有各种不同钩子函数的实现，但是要主要函数输入输出必须保持原有程序中一致，比如这里是content
    content_stash.register_input_filter_hook(input_filter_hook)

    # 执行流程
    print(content_stash.input_pipeline(content))


if __name__ == '__main__':
    main()
