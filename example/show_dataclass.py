# -*- coding:utf-8 -*-
# @Time : 2022/4/23 10:48 下午
# @Author : huichuan LI
# @File : show_dataclass.py
# @Software: PyCharm
#
# from collections import namedtuple
#
# persons = []
# person = namedtuple("Person", "name age Location weight".split())
#
#
# class Person:
#
#     def __init__(self, name, age, location, weight):
#         self.name = name
#         self.age = age
#         self.age = age
#         self.age = age
#
#
# person.age = 10
# person.name = 'some'

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: str
    location: [int, int]
    weight: float


person = Person("Jack", 10, [10, 21], 43.0)
print(person)
