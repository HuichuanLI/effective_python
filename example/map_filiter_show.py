# -*- coding:utf-8 -*-
# @Time : 2022/4/23 11:08 下午
# @Author : huichuan LI
# @File : map_filiter_show.py
# @Software: PyCharm
import random


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


perons = [Person('test', random.randint(10, 20)) for _ in range(10)]

print(perons)
persons = [p.age + 1 for p in perons]
print(persons)


def add_age(p):
    p.age += 1
    return p


def reverse_name(p):
    p.name = p.name[::-1]
    return p


returned = map(reverse_name,
               map(add_age, perons))

returned = filter(lambda n: n >= 50,
                  map(lambda n: n ** 2,
                      map(lambda p: p.age, perons)))

next(returned)

r = map(add_age, perons)
print(next(r))
print(next(r))
print(next(r))
print(next(r))

for i in map(add_age, perons):
    print(i)


class Data:
    def __init__(self, initialized):
        self.index = 0
        self.memory.append(initialized)

    def __getitem__(self, i):
        return self.memory[i]


data = Data([1, 2, 3, 4, 5])
data[0]
for d in data:
    print(d)
