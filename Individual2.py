# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Реализовать класс-оболочку Number для числового типа float. Реализовать методы
# умножения и вычитания. Создать производный класс Real, в котором реализовать метод,
# вычисляющий корень произвольной степени, и метод для вычисления числа PI в данной
# степени.


import math


class Number:
    def __init__(self, num1=0, num2=0):
        self.num1 = float(num1)
        self.num2 = float(num2)
        self.multiplication = 0
        self.subtraction = 0

        self.Calculations()

    def Calculations(self):
        self.multiplication = self.num1 * self.num2
        self.subtraction = self.num1 - self.num2

    def read(self):
        num1 = input('Enter number1: ')
        num2 = input('Enter number2: ')

        self.num1 = float(num1)
        self.num2 = float(num2)
        self.Calculations()

    def display(self):
        print(f"Multiplication: {self.multiplication}")
        print(f"Subtraction(num1-num2): {self.subtraction}")


class Real(Number):
    def __init__(self, num3=0, degree=1):
        super(Real, self).__init__()
        self.num3 = float(num3)
        self.degree = float(degree)
        self.radical = 0
        self.Pi = 0

        self.arbitraryRadical()
        self.degreeCalculating()

    def arbitraryRadical(self):
        self.radical = pow(self.num3, (1 / self.degree))

    def degreeCalculating(self):
        self.Pi = math.pi ** self.degree

    def read(self):
        num3 = input('Enter number3: ')
        degree = input('Enter degree: ')

        self.num3 = float(num3)
        self.degree = float(degree)

        self.arbitraryRadical()
        self.degreeCalculating()

    def display(self):
        print(f"Radical: {self.radical}")
        print(f"degreeCalculating: Pi={self.Pi}")


if __name__ == '__main__':
    r1 = Number()
    r1.read()
    r1.display()

    r2 = Real()
    r2.read()
    r2.display()
