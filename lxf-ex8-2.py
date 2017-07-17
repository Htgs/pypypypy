#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
math.sqrt(2) # 2的平方根

def quadratic(a, b, c):
    for x in (a, b, c):
        if not isinstance(x, (int, float)):
            raise TypeError('type must be int ot float')
    if (a == 0):
        return '无解'
    elif (b ** 2 - 4 * a * c < 0):
        return '无解'
    elif (b ** 2 - 4 * a * c == 0):
        x1 = - b/(2 * a)
        return x1
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return x1, x2

print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)

ta = (float)(input('a\n'))
tb = (float)(input('b\n'))
tc = (float)(input('c\n'))

if (quadratic(ta, tb, tc)):
    print(quadratic(ta, tb, tc))