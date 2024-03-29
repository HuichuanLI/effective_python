# -*- coding:utf-8 -*-
# @Time : 2022/4/20 9:29 下午
# @Author : huichuan LI
# @File : fib5.py
# @Software: PyCharm
def fib5(n: int) -> int:
    if n == 0: return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next


if __name__ == "__main__":
    print(fib5(5))
    print(fib5(50))
