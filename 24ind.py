#!/usr/bin/env python3
# -*- config: utf-8 -*-

import math
from threading import Thread


def sm_first(x, n):
    return (x ** (4 * n + 1)) / (4 * n + 1)


def first(x, n):
    n = n
    x = x
    eps = 1.0E-7
    previous = 0

    current = sm_first(x, n)
    n += 1
    test = (1 / 4) * math.log((1 + x) / (1 - x)) + (1 / 2) * math.atan(x)

    while math.fabs(current - previous) > eps:
        previous = current
        current = current + sm_first(x, n)
        n += 1
        print(n)


    current = round(current, 6)
    test = round(test, 6)
    if current == test:
        print(f'Сумма ряда {current} = проверочному значению {test}')


def sm_second(x, n):
    return ((-1) ** n) * x ** (2 * n) / math.factorial(2 * n)


def second(x, n):
    n = n
    x = x
    eps = 1.0E-7
    previous = 0

    current = sm_second(x, n)
    n += 1
    test = math.cos(x)

    while math.fabs(current - previous) > eps:
        previous = current
        current = current + sm_second(x, n)
        n += 1
        print(n)

    current = round(current, 6)
    test = round(test, 6)
    if current == test:
        print(f'Сумма ряда {current} = проверочному значению {test}')


if __name__ == '__main__':
    th2 = Thread(target=second(0.3, 0))
    th1 = Thread(target=first(0.5, 0))

    th1.start()
    th2.start()
