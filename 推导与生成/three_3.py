# -*- coding:utf-8 -*-
# @Time : 2022/4/26 22:11
# @Author : huichuan LI
# @File : three_3.py
# @Software: PyCharm
import sys
from contextlib import contextmanager


@contextmanager
def context_demo(para: str):
    """使用 contextmanager 装饰器让这个函数支持上下文管理"""
    f = None
    try:
        print("******enter context_demo:{}".format(para))
        f = open(sys.argv[0], mode="r", encoding="utf-8")

        yield f  # 必要的返回语句，与 __enter__ 中的 return 类似

    finally:
        print("______exit context_demo:{}".format(para))
        if f is not None:
            f.close()


if __name__ == "__main__":
    with context_demo("test") as f:
        for line in f:
            print(line, end="")
