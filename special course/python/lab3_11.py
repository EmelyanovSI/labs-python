# Emelyanov SI Lab3

# 11. Пользователь вводит матрицу A размера 3х4 и матрицу B. Посчитать значение выражения (5A+3B)

import numpy as np

A = []
B = []
print("Input first array:")
for i in range(3):
    A.append([int(j) for j in input().split()])
print("Input second array:")
for i in range(3):
    B.append([int(j) for j in input().split()])
A = np.array(A)
B = np.array(B)
res = A.dot(5) + B.dot(3)
print("Result:\n", res)
