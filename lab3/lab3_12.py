# Emelyanov SI Lab3

# 12. Пользователь вводит 3 квадратных матрицы A, B, C.
# Вычислить значение выражения (3A+2B+C) и вывести, является ли получившаяся матрица единичной.

import numpy as np

A = []
B = []
C = []
n = int(input("Input n: "))
print("Input first array:")
for i in range(n):
    A.append([int(j) for j in input().split()])
print("Input second array:")
for i in range(n):
    B.append([int(j) for j in input().split()])
print("Input third array:")
for i in range(n):
    C.append([int(j) for j in input().split()])
A = np.array(A)
B = np.array(B)
C = np.array(C)
res = A.dot(3) + B.dot(2) + C
print("Result equiv: ", np.array_equiv(res, np.eye(n, dtype=int)))
# Lab3 end
