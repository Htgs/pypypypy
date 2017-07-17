#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

#py 3 不同类型之间做比较必须转换成同一类型
num = randint(1, 100)
bingo = False
print ('guess num')

while bingo == False:
    #循环体可以包含一个语句，也可以包含多个语句，但是却不可以没有任何语句。那么，如果我们只是想让程序循环一定次数，但是循环过程什么也不做的话， 那该怎么办呢？当然是有办法的，因为Python为我们提供了一个pass语句，该语句什么也不做，也就是说它是一个空操作
    # pass
    answer = input()
    if int(answer) < num:
        print ('too small')

    if int(answer) > num:
        print ('too large')

    if int(answer) == num:
        print ('bingo')
        bingo = True