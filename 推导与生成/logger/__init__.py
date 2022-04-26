# -*- coding:utf-8 -*-
# @Time : 2022/4/26 21:56
# @Author : huichuan LI
# @File : __init__.py.py
# @Software: PyCharm
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(filename)s%(funcName)s(%(lineno)d)[%(thread)d]-[%(levelname)s]%(message)s'
)
