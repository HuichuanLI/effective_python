# -*- coding:utf-8 -*-
# @Time : 2022/4/17 8:08 下午
# @Author : huichuan LI
# @File : format.py
# @Software: PyCharm
a = 0b10111011
b = 0xc5f
print('Binary is %d, hex is %d' % (a, b))

pantry = [
    ('avocados', 1.25),
    ('bananas', 2.5),
    ('cherries', 15),
]
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (i, item, count))

key = 'my_var'
value = 1.234

old_way = '%-10s = %.2f' % (key, value)

new_way = '%(key)-10s = %(value).2f' % {
    'key': key, 'value': value}  # Original

reordered = '%(key)-10s = %(value).2f' % {
    'value': value, 'key': key}  # Swapped

assert old_way == new_way == reordered

menu = {
    'soup': 'lentil',
    'oyster': 'kumamoto',
    'special': 'schnitzel',
}
template = ('Today\'s soup is %(soup)s, '
            'buy one get two %(oyster)s oysters, '
            'and our special entrée is %(special)s.')
formatted = template % menu
print(formatted)
# Python 3 添加了高级字符串格式化（advanced string formatting）机制，它的表达能力比老式 C 风格的格式字符串要强，
# 且不再使用 % 操作符。我们针对需要调整格式的这个 Python 值，调用内置的 format 函数，并把这个值所应具备的格式也传给该函数，即可实现格式化。
# 下面这段代码，演示了这种新的格式化方式。在传给 format 函数的格式里面，逗号表示显示千位分隔符（thousands separator），^ 表示居中对齐。
a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

b = 'my string'
formatted = format(b, '^20s')
print('*', formatted, '*')

key = 'my_var'
value = 1.234
formatted = '{} = {}'.format(key, value)
print(formatted)

print('%.2f%%' % 12.5)
print('{} replaces {{}}'.format(1.23))

key = 'my_var'
value = 1.234
formatted = '{1} = {0}'.format(key, value)
print(formatted)

for i, (item, count) in enumerate(pantry):
    old_style = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count))

    new_style = '#{}: {:<10s} = {}'.format(
        i + 1,
        item.title(),
        round(count))

    assert old_style == new_style
