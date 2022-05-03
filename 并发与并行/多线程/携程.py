# -*- coding:utf-8 -*-
# @Time : 2022/5/2 13:51
# @Author : huichuan LI
# @File : 携程.py
# @Software: PyCharm
import time
import asyncio


def one():
    start = time.time()

    @asyncio.coroutine
    def do_some_work():
        print('start')
        time.sleep(0.1)
        print('this is a coroutine')

    loop = asyncio.get_event_loop()
    coroutine = do_some_work()  # 5

    loop.run_until_complete(coroutine)  # 6
    end = time.time()

    print('运行耗时：{:.4f}'.format(end - start))


one()


def two():
    start = time.time()

    @asyncio.coroutine
    def do_some_work():
        print('Start coroutine')
        time.sleep(0.1)
        print('This is a coroutine')

    loop = asyncio.get_event_loop()
    coroutine = do_some_work()
    task = loop.create_task(coroutine)  # 1
    print('task 是不是 asyncio.Task 的实例？', isinstance(task, asyncio.Task))  # 2
    print('Task state:', task._state)  # 3
    loop.run_until_complete(task)  # 4
    print('Task state:', task._state)

    end = time.time()
    print('运行耗时：{:.4f}'.format(end - start))


two()


def three():
    start = time.time()

    # @asyncio.coroutine
    async def corowork():  # 1
        print('[corowork] Start coroutine')
        time.sleep(0.1)
        print('[corowork] This is a coroutine')

    def callback(name, task):  # 2
        print('[callback] Hello {}'.format(name))
        print('[callback] coroutine state: {}'.format(task._state))

    loop = asyncio.get_event_loop()
    coroutine = corowork()
    task = loop.create_task(coroutine)
    task.add_done_callback(functools.partial(callback, 'Shiyanlou'))  # 3
    loop.run_until_complete(task)

    end = time.time()
    print('运行耗时：{:.4f}'.format(end - start))


import functools

three()


def four():
    start = time.time()

    async def corowork(name, t):
        print('[corowork] Start coroutine', name)
        await asyncio.sleep(t)  # 1
        print('[corowork] Stop coroutine', name)
        return 'Coroutine {} OK'.format(name)  # 2

    loop = asyncio.get_event_loop()
    coroutine1 = corowork('ONE', 3)  # 3
    coroutine2 = corowork('TWO', 1)  # 3
    task1 = loop.create_task(coroutine1)  # 4
    task2 = loop.create_task(coroutine2)  # 4
    gather = asyncio.gather(task1, task2)  # 5
    loop.run_until_complete(gather)  # 6
    print('[task1] ', task1.result())  # 7
    print('[task2] ', task2.result())  # 7
    end = time.time()
    print('运行耗时：{:.4f}'.format(end - start))


four()
