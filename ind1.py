#!/usr/bin/env python3
# -*- config: utf-8 -*-

import math


def sm(x, n):
    return x ** n


if __name__ == '__main__':
    n = 0
    x = 0.7
    eps = 1.0E-7
    previous = 0

    current = sm(x, n)
    n += 1
    test = 1/(1 - x)

    while math.fabs(current - previous) > eps:
        previous = current
        current = current + sm(x, n)
        n += 1

    current = round(current, 6)
    test = round(test, 6)
    print(current)
    print(test)
    if current == test:
        print('DAMN BOYY')
