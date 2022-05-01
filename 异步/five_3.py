# -*- coding:utf-8 -*-
# @Time : 2022/4/26 22:43
# @Author : huichuan LI
# @File : five_3.py
# @Software: PyCharm
"""
@author: shlian
@wechat: 312519777
@file: five_3.py
@date: 2021/1/13 9:43
@desc:
"""
import asyncio


async def hello(index: int):
    print("sleeping...", index)
    await asyncio.sleep(1)
    print("hello world!")


async def entery():
    await hello(0)
    await hello(1)
    await hello(2)


if __name__ == "__main__":
    asyncio.run(entery())
