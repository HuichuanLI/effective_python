# -*- coding:utf-8 -*-
# @Time : 2022/4/20 9:28 下午
# @Author : huichuan LI
# @File : fib4.py
# @Software: PyCharm
from functools import lru_cache


@lru_cache(maxsize=None)
def fib4(n: int) -> int:  # same definition as fib2()
    if n < 2:  # base case
        return n
    return fib4(n - 2) + fib4(n - 1)  # recursive case


if __name__ == "__main__":
    print(fib4(5))
    print(fib4(50))
