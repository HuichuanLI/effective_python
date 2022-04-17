# -*- coding:utf-8 -*-
# @Time : 2022/4/17 8:32 下午
# @Author : huichuan LI
# @File : 多线程2.py
# @Software: PyCharm
import select
import socket
import time
from threading import Thread


def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)


start = time.time()

for _ in range(5):
    slow_systemcall()

end = time.time()
delta = end - start
print(f'Took {delta:.3f} seconds')

# 执行阻塞式IO

start = time.time()

threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)


def compute_helicopter_location(index):
    pass


for i in range(5):
    compute_helicopter_location(i)

for thread in threads:
    thread.join()

end = time.time()
delta = end - start
print(f'Took {delta:.3f} seconds')
# 与依次执行系统调用的那种写法相比，这种写法的速度几乎能达到原来的 5 倍。这说明，
# 尽管那 5 条线程依然受 GIL 制约，但它们所发起的系统调用是可以各自向前执行的。GIL 只不过是让 Python 内部的代码无法平行推进而已，至于系统调用，则不会受到影响，
# 因为 Python 线程在即将执行系统调用时，会释放 GIL，待完成调用之后，才会重新获取它。


