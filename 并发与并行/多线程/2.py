# -*- coding:utf-8 -*-
# @Time : 2022/5/2 12:31
# @Author : huichuan LI
# @File : 2.py
# @Software: PyCharm
def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    yield a


f = fibonacci(100)
for i in f:
    print(i)

import inspect


def generator():
    i = '激活生成器'
    while True:
        try:
            value = yield i
        except ValueError:
            print('OVER')
            i = value


g = generator()

inspect.getgeneratorstate(g)

next(g)

inspect.getgeneratorstate(g)

g.send('hello')
g.throw(ValueError)

g.close()
inspect.getgeneratorstate(g)
