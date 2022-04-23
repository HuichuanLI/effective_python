# -*- coding:utf-8 -*-
# @Time : 2022/4/23 11:39 下午
# @Author : huichuan LI
# @File : decorator_show.py
# @Software: PyCharm
from functools import cache


@cache
def caculate_matrix(n):
    pass


def memory(f):
    memory.cache = {}  # function attribute

    def _wrap(n):
        if n in memory.cache:
            print("hit {}".format(n))
            return memory.cache[n]
        else:
            memory.cache[n] = f(n)
            return memory.cache[n]

    return _wrap


@memory
def fib(n):
    return fib(n - 1) + fib(n - 2) if n >= 2 else 1


# fib = memory(fib)
print(fib(10))


def change_result_to_none(f):
    def _wrap(*args, **kwargs):
        return None

    return _wrap


@change_result_to_none
def fib(n):
    return fib(n - 1) + fib(n - 2) if n >= 2 else 1


print(fib(10))
