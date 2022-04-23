# -*- coding:utf-8 -*-
# @Time : 2022/4/23 8:13 下午
# @Author : huichuan LI
# @File : test1.py
# @Software: PyCharm

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for x in a:
    squares.append(x ** 2)

print(squares)

squares = [x ** 2 for x in a]  # List comprehension
print(squares)

alt = map(lambda x: x ** 2, a)

even_squares = [x ** 2 for x in a if x % 2 == 0]
print(even_squares)

alt = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)

even_squares_dict = {x: x ** 2 for x in a if x % 2 == 0}
threes_cubed_set = {x ** 3 for x in a if x % 3 == 0}
print(even_squares_dict)
print(threes_cubed_set)

alt_dict = dict(map(lambda x: (x, x ** 2),
                    filter(lambda x: x % 2 == 0, a)))
alt_set = set(map(lambda x: x ** 3,
                  filter(lambda x: x % 3 == 0, a)))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

squared = [[x ** 2 for x in row] for row in matrix]
print(squared)

my_lists = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
]
flat = [x for sublist1 in my_lists
        for sublist2 in sublist1
        for x in sublist2]
print(flat)

flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)

print(flat)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
print(filtered)
