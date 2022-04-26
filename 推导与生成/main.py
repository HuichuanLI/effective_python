# -*- coding:utf-8 -*-
# @Time : 2022/4/26 21:57
# @Author : huichuan LI
# @File : main.py
# @Software: PyCharm
# coding:utf-8
from logger.logger import *


@Debug
def test_debug(*args, **kwargs):
    pass


@Info
def test_info(*args, **kwargs):
    pass


@Warning
def test_warning(*args, **kwargs):
    pass


@Error
def test_error(*args, **kwargs):
    pass


@Critical
def test_critical(*args, **kwargs):
    pass


@Debug
def sum(*args):
    res = 0
    for item in args:
        res += item
    return res


if __name__ == "__main__":
    test_debug("hello", "world", "Debug decorator")
    test_info("1+2")
    test_warning()
    test_error()
    test_critical()

    res = sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    logging.info(res)
