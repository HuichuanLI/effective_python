# -*- coding:utf-8 -*-
# @Time : 2022/4/26 22:35
# @Author : huichuan LI
# @File : 杨辉三角.py
# @Software: PyCharm
"""
@author: shlian
@contact: class7class@163.com
@file: four_6.py
@date: 2020/12/16 16:30
@desc:
"""


class pascal_triangle_based_iterator(object):
    """基于迭代器的杨辉三角"""

    def __init__(self, level_count=10):
        self._level_count = level_count
        self._sequence = [1]
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index == 1:
            return self._sequence
        elif self._index <= self._level_count:
            current_sequence = [1]
            left_num = 1
            for item in self._sequence[1:]:  # 通过上一层序列的值计算当前层的序列
                current_sequence.append(left_num + item)
                left_num = item
            current_sequence.append(1)  # 当前层的序列
            self._sequence = current_sequence
            return self._sequence
        else:
            raise StopIteration


def pascal_triangle_based_generator(level_count=10):
    """基于生成器的杨辉三角"""
    sequence = [1]
    for index in range(1, level_count + 1):
        if index == 1:
            yield sequence
        else:
            current_sequence = [1]
            left_num = 1
            for item in sequence[1:]:
                current_sequence.append(left_num + item)
                left_num = item
            current_sequence.append(1)
            sequence = current_sequence
            yield sequence


if __name__ == "__main__":
    pascaler = pascal_triangle_based_iterator(level_count=10)
    print("基于迭代器的杨辉三角：")
    for item in pascaler:
        print(" ", f"{item}".center(40, " "))
    print()

    print("基于生成器的杨辉三角：")
    pascaler = pascal_triangle_based_generator(level_count=10)
    for item in pascaler:
        print(" ", f"{item}".center(40, " "))
    print()
