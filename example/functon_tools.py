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
from functools import cache, lru_cache, cached_property, total_ordering, partial, singledispatchmethod


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

import random


@total_ordering
class Hero:
    def __init__(self, name, live=None, magic=None):
        self.name = name
        self.live = live or random.randint(0, 100)
        self.magic = magic or random.randint(0, 100)

    def __lt__(self, other):
        return (self.live, self.magic) < (other.live, other.magic)

    def __eq__(self, other):
        return (self.live, self.magic) == (other.live, other.magic)


print(reduce(type_op[type(some_lists)], some_lists))


@singledispatchmethod
def multiply(arg1, arg2):
    return arg1 * arg2


@multiply.register
def _(arg1: int, arg2: int):
    return arg1 * arg2


@multiply.register
def _(arg1: str, arg2: str): return arg1


@multiply.register
def _(arg1: list, arg2: list):
    assert len(list) == len(arg2)
    return [a1 * a2 for a1, a2 in zip(arg1, arg2)]




if __name__ == "__main__":
    print(reduce(lambda a, b: op.add(a, b), some_lists))

    li_bai = Hero('libai')
    cao = Hero(' caocao')
    hunter = Hero('deman-hunter')
    master = Hero('blood-master')
    print(li_bai, cao, hunter, master)
    print(Hero('libai', 11, 10) >= Hero('caocao', 10, 10))

    agent_1_conflg = {
        "agent_id": 'agent_01',
        "agent_name": "jack",
        "agent_env": 'foot_ball',
        "agent_action_space":
            list(range(6))}

    load_agent_1_obs = partial(load_training_info, **agent_1_config)
    print(load_agent_1_obs)
    multiply(3, 'test')
    multiply([3, 4, 5], [4, 5, 6])  # [12, 20, 30]
    multiply('4', 'test')
