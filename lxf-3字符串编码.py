#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码

print('包含了什么鬼？str')
# 对于单个字符的编码
# Python提供了ord()函数获取字符的整数表示
print(ord('A'))
print(ord('总'))
# chr()函数把编码转换为对应的字符
print(chr(66))
print(chr(32984))
print('\u4e2d\u6587') # 中文


bb = b'QaQ' # bytes类型 用于网络上传输，或者保存到磁盘上
b = 'QaQ' #str类型
print('QaQ'.encode('utf-8')) #str通过encode()方法可以编码为指定的bytes
print(b'QaQ'.decode('utf-8')) #bytes通过decode()方法转为str

# len()函数计算的是str的字符数
print(len(b))
print(len(bb.decode('utf-8'))) #bytes需要转换为str类型才能使用len方法

# 占位符
# %d    整数
# %f  浮点数
# %s  字符串
# %x  十六进制整数
print('hi,%s,you have '%'da')
print('hi,%s,you have $%d.'%('bbbb', 9999))
print('growth rate: %d %%' %(9999)) # 用%%来表示一个%
