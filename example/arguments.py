# -*- coding:utf-8 -*-
# @Time : 2022/4/23 11:26 下午
# @Author : huichuan LI
# @File : arguments.py
# @Software: PyCharm
def combine(elements):
    return sum(elements)


def configure(arguments):
    for k, V in arguments:
        print(k, V)


def configure_s(*arg):
    print(arg)


def configure_ks(**kwargs):
    print(kwargs)


def get_config_info():
    return ('Length', 3), ('level', 4), ('security', 10)


def function_with_three_arguments(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


def control_by_configure(length, Level, security):
    print(length, Level, security)


def function_with_arbitary_arguments(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == "__main__":
    arguments = [('length', 3), ('level', 4), ('security', 10)]
    configure(arguments)
    function_with_three_arguments(*arguments)

    configure_s(('length', 3), ('level', 4), ('security', 10))
    configure_ks(length=3, level=3, security=10)

    configure_map = {
        "Level": 3,
        "length": 3,
        "security": 10,
    }

    control_by_configure(**configure_map)

    function_with_arbitary_arguments(10, 20, 30, key=10, age=20, same=False, )
