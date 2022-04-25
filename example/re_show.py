# -*- coding:utf-8 -*-
# @Time : 2022/4/24 10:36 下午
# @Author : huichuan LI
# @File : re_show.py
# @Software: PyCharm

import re

some_text = "I am a good man!"

re.findall('\w', some_text)

some_text = "~~~~~~I am a good man!"

re.findall('\w', some_text)
re.findall('\w+', some_text)

some_text = "I am a good man, but you are a very foolish man!"
re.findall('o+', some_text)

re.findall('\W', some_text)

some_text = "I am a good man, and I have 21 friends; but you are a very foolish man, you just have 1 friend!"

re.findall('\d+', some_text)


def token(string):
    return re.findall('\w*!, string)

for i, line in enumerate(file):
    if i >= length:
        break
    tokens = token(line)
    print(tokens)
