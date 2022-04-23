# -*- coding:utf-8 -*-
# @Time : 2022/4/23 10:55 下午
# @Author : huichuan LI
# @File : yield.py
# @Software: PyCharm

import time
from collections import defaultdict


def count_words(filename):
    counts = defaultdict(int)
    time.sleep(1)
    return counts


def get_all_results(files):
    results = []
    # for f in files:
    #     # results.append(count_words(f))
    #     yield count_words(f)
    # return results
    return (count_words(f) for f in files)


def collect_results(files):
    results = defaultdict(int)

    for c in get_all_results(files):
        print('get_one')
        for k, v in c:
            results[k] += v


if __name__ == "__main__":
    files = ['file'] * 4
    collect_results(files)
