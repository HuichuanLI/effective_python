# -*- coding:utf-8 -*-
# @Time : 2022/5/2 12:45
# @Author : huichuan LI
# @File : 3.py
# @Software: PyCharm
from functools import wraps
import inspect


# 预激活函数
def coroutine(func):
    @wraps(func)
    def wrapper(*args, **kw):
        g = func(*args, **kw)
        next(g)
        return g

    return wrapper


@coroutine
def generator():
    i = '激活生成器'
    while True:
        try:
            value = yield i
        except ValueError:
            print('Over')
        i = value


g = generator()

print(inspect.getgeneratorstate(g))


@coroutine
def generator():
    l = []
    while True:
        value = yield
        if value == 'close':
            break
        l.append(value)
    return l


g = generator()

for i in ('hello', 'shiyanlou1', 'close'):
    try:
        g.send(i)
    except StopIteration as e:
        value = e.value
        print('end')

print(value)

from itertools import chain

c = chain({'one', 'two'}, list('ace'))

for i in c:
    print(i)


def chain1(*args):
    for iter_obj in args:
        for i in iter_obj:
            yield i


c = chain1({'one', 'two'}, list('ace'))

for i in c:
    print(i)


def chain2(*args):
    for iter_obj in args:
        yield from iter_obj


c = chain2({'one', 'two'}, list('ace'))

for i in c:
    print(i)
