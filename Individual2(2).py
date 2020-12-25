# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Реализовать класс-оболочку Number для числового типа float. Реализовать методы
# умножения и вычитания. Создать производный класс Real, в котором реализовать метод,
# вычисляющий корень произвольной степени, и метод для вычисления числа PI в данной
# степени.


import math


class Number:
    def __init__(self, num=0):
        self.num = float(num)

    def truediv(self, other):
        return Number(self.num / other.num)

    def sub(self, other):
        return Number(self.num - other.num)


class Real(Number):
    def super(Real, self).__init__(num):
        self.num = float(num)

    def sqrtn(self, n):
        return self.num ** (1 / n)


if __name__ == '__main__':
    r1 = Number(3)
    r2 = Real(5)

    print(r1.truediv(r1/r2))
