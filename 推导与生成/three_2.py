# -*- coding:utf-8 -*-
# @Time : 2022/4/26 22:08
# @Author : huichuan LI
# @File : three_2.py
# @Software: PyCharm
import datetime


class context_simple_demo(object):
    """一个简单的支持上下文管理的类"""

    def __init__(self):
        """构造函数，在创建对象的时候被调用"""
        print("Creat one object")
        self._birthday = datetime.datetime.now()

    def __enter__(self):
        """申请资源，这里只打印函数调用的信息"""
        print("Invoke __enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """释放资源，这里只打印函数调用的信息"""
        print("Invoke __exit__")
        if exc_type:
            print("exc_type:{}".format(exc_type))
            print("exc_val:{}".format(exc_val))
            print("exc_tb:{}".format(exc_tb))

    @property
    def birthday(self):
        return self._birthday


if __name__ == "__main__":
    with context_simple_demo() as csd:
        # 与 context_simple_demo 相关的业务逻辑代码
        print(csd.birthday)
        # raise Exception("raise an exception")
