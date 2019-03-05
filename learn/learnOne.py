# Emelyanov SI learn
import random
from math import pi, sqrt
# from math import * - использовать не рекомендуется
# import mailbox as mb
# from math import log as gol

import numpy
import tensorflow
import pandas
import svm

i = 0
j = 0
while i < 10:
    while j < 10:
        if i is j:
            print('0', end=' ')
        else:
            print('1', end=' ')
        j += 1
    i += 1
    j = 0
    print(end='\n')

arr = []
print(arr)
listArr = [7, 7, 7, 7, 7]
listArr[2] = 5
print(listArr)
print(listArr + [3, 3, 3])
print(listArr * 3)
print(5 in listArr)
strLove = "I love my parents."
print(strLove)
print("love" in strLove)
print("love so match" in strLove)
print("love" not in strLove)
print("love so match" not in strLove)

listArr.append(4)
print(listArr)
print(len(listArr))
print(listArr.index(5))

listArr = list
print(listArr)
listArr = list(range(10))
print(listArr)
listArr = list(range(1, 11))
print(listArr)
listArr = list(range(1, 20, 2))
print(listArr)

print()
words = ["One", "Two", "Three", "Four", "Five", "Six", "Seven"]
for word in words:
    print(word + "!")

for i in range(5):
    print(i + 1, end=' ')

# little calculator
# while True:
#     print("\n1.Add\n2.Sub\n3.Mul\n4.Del\nn.Exit\n")
#     number = int(input("Input number of operation: "))
#     if number < 1 or number > 4:
#         print("Выхожу...")
#         break
#     a = float(input("Input a: "))
#     b = float(input("Input b: "))
#     if number is 1:
#         print("Res of add: " + str(a + b))
#     elif number is 2:
#         print("Res of sub: " + str(a - b))
#     elif number is 3:
#         print("Res of mul: " + str(a * b))
#     elif number is 4:
#         print("Res of del: " + str(a / b))
# end of little calculator

''' Функции '''


def calc():
    """
    :return:
    """
    while True:
        print("\n1.Add\n2.Sub\n3.Mul\n4.Del\nn.Exit\n")
        number = int(input("Input number of operation: "))
        if number < 1 or number > 4:
            print("Выхожу...")
            break
        a = float(input("Input a: "))
        b = float(input("Input b: "))
        if number is 1:
            print("Res of add: " + str(a + b))
        elif number is 2:
            print("Res of sub: " + str(a - b))
        elif number is 3:
            print("Res of mul: " + str(a * b))
        elif number is 4:
            print("Res of del: " + str(a / b))


calc()


def calc2(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    print("\n1.Add\n2.Sub\n3.Mul\n4.Del\nn.Exit\n")
    number = int(input("Input number of operation: "))
    if number is 1:
        print("Res of add: " + str(a + b))
    elif number is 2:
        print("Res of sub: " + str(a - b))
    elif number is 3:
        print("Res of mul: " + str(a * b))
    elif number is 4:
        print("Res of del: " + str(a / b))
    else:
        print("Выхожу...")
    return "EOF"


strCalc2 = calc2(3, 3)
print(strCalc2)


def add(x, y):
    return x + y


def twice(func, x, y):
    return func(func(x, y), func(x, y))


a = 5
b = 10
print(twice(add, a, b))

print("RANDOM:")
# 1 - 6 диапазон
for i in range(5):
    value = random.randint(1, 6)
    print(value)

print(pi)


lab101 = numpy.eye(10)
print(lab101)

