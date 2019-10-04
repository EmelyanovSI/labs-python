# Emelyanov SI Lab2

# 21. Ввести матрицу 3х3, транспонировать и умножить на исходную.

import numpy as np

arr = []
print("\nInput array:")
for i in range(3):
    arr.append([int(j) for j in input().split()])
arr = np.array(arr)
arr = arr.transpose() * arr
print("Result:")
print(arr)
