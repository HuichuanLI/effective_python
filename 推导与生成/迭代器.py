# -*- coding:utf-8 -*-
# @Time : 2022/4/26 22:23
# @Author : huichuan LI
# @File : 迭代器.py
# @Software: PyCharm
"""
@author: shlian
@contact: class7class@163.com
@file: four_1.py
@date: 2020/12/9 10:36
@desc:
"""


class iterator_counter(object):
    """声明一个获取迭代次数的类"""

    def __init__(self, max_iter_count=10):
        self._iter_count = 0
        self._max_iter_count = max_iter_count

    def __next__(self):
        """实现 __next__ 方法，让这个类的对象支持迭代"""
        # 当迭代次数大于等于 _max_iter_count 时，则抛出异常以终止循环
        if self._iter_count >= self._max_iter_count:
            raise StopIteration
        else:
            self._iter_count += 1
            return self._iter_count

    def __iter__(self):
        return self


if __name__ == "__main__":
    rn = iterator_counter()
    print(next(rn))  # 进行一次迭代，next 函数会调用 iterator_counter 类的 __next__ 方法
    print(next(rn))  # 进行一次迭代
    print(next(rn))  # 进行一次迭代
    print(next(rn))  # 进行一次迭代

    print("Enter for loop:")
    for num in rn:
        print(num)
