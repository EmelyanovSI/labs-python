# Emelyanov SI Lab1

# 8. Пользователь вводит две квадратные матрицы, посчитать абсолютную величину разности из определителей.

import tensorflow as tf


def array_length():
    while True:
        length = input("Input n: ")
        if length.isdigit():
            length = int(length)
            if length > 0:
                return length
            else:
                print("Array length must be higher than 0, try again!")
        else:
            print("Input error, try again!")


def array_input(length, num):
    print("Input", num, "array:")
    arr = []
    while True:
        for i in range(length):
            arr.append([is_number(j) for j in input().split(None, length - 1)])
            if len(arr[i]) == length:
                continue
            else:
                arr = []
                print("Length error! Try input " + str(length) + " element(s)")
                print("Input array:")
                break
        if arr:
            return arr


def is_number(j):
    if j.isdigit():
        return float(j)
    elif j.split()[0].isdigit():
        return float(j.split()[0])
    else:
        print("String input was skipped! Zero instead.")
    return 0


n = array_length()
arr1 = array_input(n, 1)
arr2 = array_input(n, 2)
matrix_1 = tf.Variable(arr1)
matrix_2 = tf.Variable(arr2)
det = tf.Variable(tf.math.abs(tf.linalg.det(matrix_1) - tf.linalg.det(matrix_2)))
print("Result:", det)
