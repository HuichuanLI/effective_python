# -*- coding:utf-8 -*-
# @Time : 2022/4/26 22:41
# @Author : huichuan LI
# @File : five_1.py
# @Software: PyCharm
import asyncio


async def coroutine_func(index: int):
    print(f"Start a new coroutine,index={index}")
    await asyncio.sleep(1)
    print(f"Exit coroutine,index={index}")


if __name__ == "__main__":
    asyncio.run(coroutine_func(1))  # 创建一个事件循环，运行协程 coroutine_func(1) ，最后关闭事件循环
    asyncio.run(coroutine_func(2))  # 创建一个事件循环，运行协程 coroutine_func(2) ，最后关闭事件循环
