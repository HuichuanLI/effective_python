# -*- coding:utf-8 -*-
# @Time : 2022/4/17 8:36 下午
# @Author : huichuan LI
# @File : gil.py
# @Software: PyCharm
from threading import Lock


class Counter:
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset


def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        # Read from the sensor
        counter.increment(1)


from threading import Thread

how_many = 10 ** 5
counter = Counter()

threads = []
for i in range(5):
    thread = Thread(target=worker,
                    args=(i, how_many, counter))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

expected = how_many * 5
found = counter.count
print(f'Counter should be {expected}, got {found}')
