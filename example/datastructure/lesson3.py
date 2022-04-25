# -*- coding:utf-8 -*-
# @Time : 2022/4/24 11:58 下午
# @Author : huichuan LI
# @File : lesson3.py
# @Software: PyCharm
def add(a, b):
    return a + b


class Vector:

    def __init__(self, *args):
        self._list = list(args)

    def __getitem__(self, item):
        return self._list[item]

    def __add__(self, other):
        return [self._list[i] + other[i] for i in range(len(other))]

    def __len__(self):
        return len(self._list)


from collections import namedtuple

Card = namedtuple('Card', ['number', 'shape'])

import random


class Poker:
    numbers = '234567890JQKA'
    color = '1234'
    joker = '小王 大王'.split()

    def __init__(self):
        self._cards = [Card(n, s) for n in Poker.numbers for s in Poker.color]
        self._cards.append(Card(15, Poker.joker[0]))
        self._cards.append(Card(16, Poker.joker[1]))

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value


deck = Poker()
print(deck._cards)
print(len(deck))
print(random.choice(deck))


class Person:
    count = 0

    def __init__(self, _id):
        self._id = _id
        self.count += 1


p = Person(1190)
print(p.count)
print(Person.count)

display = []
buttons = []
for n in range(10):
    print(id(n))
    buttons.append(lambda n=n: display.append(n))
print(buttons)
btn = buttons[3]
btn()
print(display)

import re
from collections import defaultdict


def word_freq(text, freqs=defaultdict(int)):
    """Calculate word frequency in text. freqs are
    previous frequencies"""
    for word in [w.lower() for w in re.findall(r'\w+', text)]:
        freqs[word] += 1
    return freqs


freqs1 = word_freq('Duck season. Duck!')
freqs2 = word_freq('Rabbit season. Rabbit!')

print(freqs1)
print(freqs2)

from functools import wraps


# def metrics(fn):
#     ncalls = 0
#     name = in._name_
#
#     @wraps(fn)
#     def wrapper(*args, **kw):
#         nonlocal ncalls
#         ncalls += 1
#
#     return wrapper


# @metrics
# def inc(n):
#     return n + 1
#

def add_n(items, n):
    items += range(n)
    return items


items = [0, 1]
add_n(items, 3)

new_item = add_n(items, 3)
new_item[-1] = 99
print(items)

print(new_item)


def new_small_func(n):
    if n > 5: n = 5
    m = 5
    return n + m


def func_small(n):
    m = 10
    return n + m


def func_complex(n):
    result = func_small(n)
    return result ** 2


import copy


def change_func_complex(func):
    def _wrap(*args, **kwargs):
        original = copy.copy(new_small_func)
        global func_small
        func_small = new_small_func
        r = func(*args, **kwargs)
        func_small = original
        return r

    return _wrap


print(func_complex(10))
func_complex_new = change_func_complex(func_complex)
print(func_complex_new(100))

import numpy as np


def softmax(vec):
    vec = vec - vec.max(vec)
    return np.exp(vec) / np.sum(np.exp(vec))
