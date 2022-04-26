# -*- coding:utf-8 -*-
# @Time : 2022/4/26 22:15
# @Author : huichuan LI
# @File : three_4.py
# @Software: PyCharm
import sys


def copy_text_file(src_file: str, dst_file: str):
    """拷贝文件，从 src_file 拷贝到 dst_file"""

    with open(file=src_file, mode="r") as src:  # 打开源文件
        with open(file=dst_file, mode="w") as dst:  # 打开目标文件
            for line in src:  # 遍历源文件的每一行
                dst.write(line)  # 把源文件的行写入到目标文件
            print("copy {} to {} successfully!".format(src_file, dst_file))


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        copy_text_file(sys.argv[1], sys.argv[2])  # argv[1] 是源文件，argv[2] 是目标文件
    else:
        print("Usage: python3.9 three_4.py src_file dst_file")  # 使用方式说明
