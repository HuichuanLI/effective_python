# -*- coding:utf-8 -*-
# @Time : 2022/4/26 22:31
# @Author : huichuan LI
# @File : 等差数列.py
# @Software: PyCharm
"""
@author: shlian
@contact: class7class@163.com
@file: four_4.py
@date: 2020/12/16 14:11
@desc:
"""


class arithmetic_sequence_based_iterator(object):
    """基于迭代器的等差数列"""

    def __init__(self, first=0, step=1, sequence_count=10):
        self._first = first
        self._step = step
        self._sequence_count = sequence_count

        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._sequence_count:
            res = self._first + self._index * self._step
            self._index += 1
            return res
        else:
            raise StopIteration


def arithemtic_sequence_based_generator(first=0, step=1, sequence_count=10):
    """基生生成器函数的等差数列，与上面的代码功能完全相同"""
    for index in range(0, sequence_count):
        yield first + index * step
        index += 1


if __name__ == "__main__":
    sequence = arithmetic_sequence_based_iterator(first=0, step=5, sequence_count=10)
    print("基于迭代器的结果：")
    for number in sequence:
        print(number, end=" ")
    print()

    print("基于生成器的结果：")
    generator = arithemtic_sequence_based_generator(first=0, step=5, sequence_count=10)
    for number in generator:
        print(number, end=" ")
    print()
