# -*- coding:utf-8 -*-
# @Time : 2022/4/20 9:25 下午
# @Author : huichuan LI
# @File : fib2.py
# @Software: PyCharm
def fib2(n: int) -> int:
    if n < 2:  # base case
        return n
    return fib2(n - 2) + fib2(n - 1)  # recursive case


if __name__ == "__main__":
    print(fib2(5))
    print(fib2(10))
