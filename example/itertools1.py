# -*- coding:utf-8 -*-
# @Time : 2022/4/24 9:23 下午
# @Author : huichuan LI
# @File : itertools1.py
# @Software: PyCharm

import itertools
from dataclasses import dataclass


@dataclass
class Model:
    lr: float
    gamma: float


class CNN(Model):
    pass


class LSTM(Model):
    pass


class GRU(Model):
    pass


def run_a_model(model_name, lr, gamma):
    model_name_mapping = {
        'CNN': CNN,
        'LSTM': LSTM,
        'GRU': GRU
    }
    print(f'running model {model_name} as {lr} {gamma}')
    acc = model_name_mapping[model_name](lr, gamma)


some_names = ['GRU', 'CNN', 'LSTM']
Lr = [1e-3, 1e-4, 3e-5, 1e-6]
gamma = [1e-3, 1e-2, 1e-1]

for p in itertools.product(some_names, Lr, gamma):
    run_a_model(*p)

for n in itertools.permutations(some_names, 2):
    print(n)

for n in itertools.combinations(some_names, 2):
    print(n)
# group by

import random

mock_login = ['uid2221', 'uid2213', 'vid2321'] * 10
random.shuffle(mock_login)

print(mock_login)

for g, elem in itertools.groupby(mock_login, key=lambda b: int(b[-1]) % 2):
    print(g, list(elem))

numbers = [2, 1, 31, 21, 41, 1, 31, 12, 1, 43, ]
print(list(itertools.accumulate(numbers, max)))
print(list(itertools.accumulate(numbers, min)))
print(list(itertools.accumulate(numbers, lambda x, y: x + y)))
