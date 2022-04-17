# -*- coding:utf-8 -*-
# @Time : 2022/4/17 8:28 下午
# @Author : huichuan LI
# @File : 多线程1.py
# @Software: PyCharm

# 奇怪的是，这样做竟然比一个一个去分解还要慢。在其他语言中，像这样令 4 条线程分别执行各自的任务，应该比一条线程连续执行 4 份任务要快得多，考虑到创建线程与协调这些线程的开销，新程序的速度可能会比旧程序的 4 倍稍微低一点。即便 CPU 的核心数量不足 4 个，新程序也还是应该比原来更快才对（例如笔者的电脑是双核的，所以应该接近原来的 2 倍），但为什么它没有把多核心的优势发挥出来？这是因为，这种多线程的程序在标准的 CPython 解释器之中会受 GIL 牵制（例如 CPython 要通过 GIL 防止这些线程争抢全局锁，而且要花一些时间来协调）。

# 其次，我们可以通过 Python 的多线程机制处理阻塞式的 I/O 任务，因为线程在执行某些系统调用的过程中会发生阻塞，假如只支持一条线程，那么整个程序就会卡在这里不动。Python 程序需要通过系统调用与外部环境交互，其中有一些调用属于阻塞式的 I/O 操作，例如读取文件、写入文件、联网以及与显示器等设备交互。多线程机制可以让程序中的其他线程继续执行各自的工作，只有发起调用请求的那条线程才需要卡在那里等待操作系统给出结果。


from threading import Thread
def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


import time

numbers = [2139079, 1214759, 1516637, 1852285]
start = time.time()

threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()
delta = end - start
print(f'Took {delta:.3f} seconds')
