# -*- coding:utf-8 -*-
# @Time : 2022/4/26 22:26
# @Author : huichuan LI
# @File : yield_from.py
# @Software: PyCharm
""""
@author: shlian
@contact: class7class@163.com
@file: four_3.py
@date: 2020/12/11 9:32
@desc:
"""


def generate_even(number_count: int = 5):
    """返回偶数序列的生成器"""
    num = 0
    for index in range(0, number_count):
        yield num
        num += 2


def generate_odd(number_count: int = 5):
    """返回奇数序列的生成器"""
    num = 1
    for index in range(0, number_count):
        yield num
        num += 2


if __name__ == "__main__":

    names = ["Tom", "Tim", "Jim", "Ada"]
    generates = [generate_even(5), generate_odd(5), names, 1234, "done."]  # 构造一个列表


    def travel_generate():  # 大家还记得之前讲过的闭包吗？
        for ele in generates:
            if hasattr(ele, '__iter__'):
                yield from ele
            else:
                yield ele


    for item in travel_generate():
        print(item, end=" ")
    print()
