# -*- coding:utf-8 -*-
# @Time : 2022/4/26 22:23
# @Author : huichuan LI
# @File : 生成器.py
# @Software: PyCharm
"""
@author: shlian
@contact: class7class@163.com
@file: four_2.py
@date: 2020/12/10 9:46
@desc:
"""


def generate_even(number_count: int = 5):
    """返回偶数序列的生成器"""
    num = 0
    for index in range(0, number_count):
        print("yield...{0}".format(num))
        # yield 与 return 不同
        # yield 的执行流程是先暂停当前函数的执行，然后返回 num 的值给调用函数
        # 调用函数执行完成后再返回到本函数的 yield 处继续执行
        yield num
        num += 2
        print("yield")


if __name__ == "__main__":
    for num in generate_even():  # 生成 5 个偶数
        print(num)

    my_list = [1, 3, 6, 10]  # 初始化一个列表

    list_ = [x ** 2 for x in my_list]  # 使用列表解析生成一个新的列表

    generator = (x ** 2 for x in my_list)  # 使用生成器表达式生成一个生成器函数

    print(list_)
    print(generator)
