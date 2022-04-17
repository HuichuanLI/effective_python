# -*- coding:utf-8 -*-
# @Time : 2022/4/17 4:52 下午
# @Author : huichuan LI
# @File : bytes.py
# @Software: PyCharm
a = b'h\x65llo'
print(a)
print(list(a))
print(type(a))

b = 'a\u0300 propos'
print(b)
print(list(b))
print(type(b))


# 如果要从文件中读取（或者要写入文件之中）的是 Unicode 数据，那么必须注意系统默认的文本编码方案。若无法肯定，可通过 encoding 参数明确指定。
# 从文件中读取二进制数据（或者把二进制数据写入文件）时，应该用 'rb'（'wb'） 这样的二进制模式打开文件。

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str


print(repr(to_str(b'foo')))
print(repr(to_str('bar')))

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))
