#!/usr/bin/env python3
# -*- config: utf-8 -*-

import math

eps = 1.0E-7
x = -0.8
n = 1
s = 1 + x
test = math.sqrt(1 + x)
while abs(x) > eps:
    n += 1
    x *= - 1 ** (n + 1) * ((2 * n - 3) / (2 * n)) * x ** n
    s += x
print(s)
print(test)
