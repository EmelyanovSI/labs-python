# Emelyanov SI Lab2
import numpy as np

arr = []
print("\nInput array:")
for i in range(3):
    arr.append([int(j) for j in input().split()])
arr = np.array(arr)
arr = arr * arr.transpose()
print("Result:")
print(arr)
# Lab2 end
