# -*- coding:utf-8 -*-
# @Time : 2022/4/17 8:27 下午
# @Author : huichuan LI
# @File : 多线程.py
# @Software: PyCharm
def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


import time

numbers = [2139079, 1214759, 1516637, 1852285]
start = time.time()

for number in numbers:
    print(list(factorize(number)))

end = time.time()
delta = end - start
print(f'Took {delta:.3f} seconds')


