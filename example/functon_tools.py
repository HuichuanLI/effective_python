# -*- coding:utf-8 -*-
# @Time : 2022/4/24 12:21 上午
# @Author : huichuan LI
# @File : functon_tools.py
# @Software: PyCharm
"""
Some useful function tools.
Speed up the dev process.
"""

from functools import reduce
import operator as op
from functools import cache, lru_cache, cached_property


@lru_cache(maxsize=2 ** 10)
def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 2 else 1


some_lists = [[1, 2],
              [3, 5],
              [5, 6, 7, 1, 10.1, 11.1],
              [121.4, 11.34],
              [11.31, 1921, 321.],
              ]

whole_list = []
for a_list in some_lists:
    whole_list.append(a_list)

type_op = {
    list: op.add,
    int: op.add,
    float: op.add,
    set: op.or_,
}

print(reduce(type_op[type(some_lists)], some_lists))
if __name__ == "__main__":
    print(reduce(lambda a, b: op.add(a, b), some_lists))
