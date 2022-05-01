# -*- coding:utf-8 -*-
# @Time : 2022/4/26 22:38
# @Author : huichuan LI
# @File : 生成器处理较.py
# @Software: PyCharm
"""
@author: shlian
@contact: class7class@163.com
@file: four_7.py
@date: 2020/12/16 11:30
@desc:
"""
import sys


def process_txt_file(file_name: str):
    """ 读取文件的生成器函数"""
    with open(file_name, mode="r", encoding="utf-8") as f:  # 上下文管理器
        line_number = 1
        for line in f:
            new_line = line.strip()
            new_line = f"{line_number} {line}"
            yield new_line
            line_number += 1


if __name__ == "__main__":
    file_name = sys.argv[0]
    for line in process_txt_file(file_name):
        print(line, end="")
    print()
