# -*- coding:utf-8 -*-
# @Time : 2022/4/26 21:46
# @Author : huichuan LI
# @File : two_2.py
# @Software: PyCharm
def prefix_ABC(f):
    '''增加ABC_前缀的装饰器'''
    prefix = "ABC_{}"

    def inner(source: str):
        '''闭包函数'''
        res = prefix.format(f(source))
        print("append_ABC:{}".format(res))
        return res

    return inner


def prefix_DEF(f):
    '''增加DEF_前缀的装饰器'''
    prefix = "DEF_{}"

    def inner(source: str):
        '''闭包函数'''
        res = prefix.format(f(source))
        print("append_DEF:{}".format(res))
        return res

    return inner


def prefix_123(f):
    '''增加123_前缀的装饰器'''
    prefix = "123_{}"

    def inner(source: str):
        '''闭包函数'''
        res = prefix.format(f(source))
        print("append_123:{}".format(res))
        return res

    return inner


@prefix_123
@prefix_ABC
@prefix_DEF
def append(source: str):
    print("append:{}".format(source))
    return source


if __name__ == '__main__':
    val = append("Python")
    print(val)
