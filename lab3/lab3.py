# Emelyanov SI Lab3

# 8. Пользователь вводит две квадратные матрицы, посчитать абсолютную величину разности из определителей.

import numpy as np

n = int(input("Input n: "))
arr1 = []
arr2 = []
print("Input first array:")
for i in range(n):
    arr1.append([int(j) for j in input().split()])
print("Input second array:")
for i in range(n):
    arr2.append([int(j) for j in input().split()])
res = abs(np.linalg.det(arr1) - np.linalg.det(arr2))
print("Result: " + str(int(res)))
# Lab3 end
