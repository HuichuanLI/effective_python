# -*- coding:utf-8 -*-
# @Time : 2022/5/2 12:25
# @Author : huichuan LI
# @File : 1.py
# @Software: PyCharm
# File Name: thread.py

import threading
import time


def crawl_url():  # 假设这是爬虫程序，爬取一个 URL
    time.sleep(0.02)  # 模拟 IO 操作


def main1():  # 单线程程序
    for i in range(100):
        crawl_url()


def main2():  # 多线程程序
    thread_list = []
    for i in range(100):
        t = threading.Thread(target=crawl_url)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()


if __name__ == '__main__':
    start = time.time()
    main1()
    end = time.time()
    print('单线程耗时：{:.4f}s'.format(end - start))
    start = time.time()
    main2()
    end = time.time()
    print('多线程耗时：{:.4f}s'.format(end - start))
