# -*- coding:utf-8 -*-
# @Time : 2022/4/26 21:29
# @Author : huichuan LI
# @File : 比包.py
# @Software: PyCharm
def outer_func(f):
    b = 10

    def inner(x: int, y: int):
        return b + f(x, y)

    return inner


def sum(x, y):
    return x + y


def outer_func(f):
    b = 10

    def inner(x: int, y: int):
        return b + f(x, y)

    return inner


@outer_func
def sum(x, y):
    return x + y


if __name__ == '__main__':
    val = sum(10, 20)
    print(val)

