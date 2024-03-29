# -*- coding:utf-8 -*-
# @Time : 2022/4/17 11:54 下午
# @Author : huichuan LI
# @File : stoke.py
# @Software: PyCharm
def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    assert False, 'Not reachable'


import time

NUMBERS = [
    (1963309, 2265973), (2030677, 3814172),
    (1551645, 2229620), (2039045, 2020802),
    (1823712, 1924928), (2293129, 1020491),
    (1281238, 2273782), (3823812, 4237281),
    (3812741, 4729139), (1292391, 2123811),
]


def main1():
    start = time.time()
    results = list(map(gcd, NUMBERS))
    end = time.time()
    delta = end - start
    print(f'Took {delta:.3f} seconds')


main1()

from concurrent.futures import ThreadPoolExecutor
import time

NUMBERS = [
    (1963309, 2265973), (2030677, 3814172),
    (1551645, 2229620), (2039045, 2020802),
    (1823712, 1924928), (2293129, 1020491),
    (1281238, 2273782), (3823812, 4237281),
    (3812741, 4729139), (1292391, 2123811),
]


def main2():
    start = time.time()
    pool = ThreadPoolExecutor(max_workers=2)
    results = list(pool.map(gcd, NUMBERS))
    end = time.time()
    delta = end - start
    print(f'Took {delta:.3f} seconds')


main2()

from concurrent.futures import ProcessPoolExecutor
import time

NUMBERS = [
    (1963309, 2265973), (2030677, 3814172),
    (1551645, 2229620), (2039045, 2020802),
    (1823712, 1924928), (2293129, 1020491),
    (1281238, 2273782), (3823812, 4237281),
    (3812741, 4729139), (1292391, 2123811),
]


def main3():
    start = time.time()
    pool = ProcessPoolExecutor(max_workers=2)  # The one change
    results = list(pool.map(gcd, NUMBERS))
    end = time.time()
    delta = end - start
    print(f'Took {delta:.3f} seconds')


main3()
