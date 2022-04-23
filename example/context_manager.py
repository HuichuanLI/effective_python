# -*- coding:utf-8 -*-
# @Time : 2022/4/24 12:18 上午
# @Author : huichuan LI
# @File : context_manager.py
# @Software: PyCharm

from contextlib import contextmanager


@contextmanager
def connect_database(url):
    obj = open(url, 'r')
    try:
        print('enter the ob')
        yield obj
    finally:
        obj.close()
        print("obj close")


with connect_database('context_manager.py') as c:
    c.read()
