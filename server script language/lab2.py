# EmelyanovSI lab2

# 6. Пользователь вводит три числа. Найти сумму тех чисел, которые делятся на 5. Если таких чисел нет, то вывести error.


def is_number(value):
    if value.isdigit():
        return int(value)
    elif value.split()[0].isdigit():
        return int(value.split()[0])
    else:
        print("String input was skipped! Zero instead.")
    return 0


try:
    arr = [is_number(i) for i in input("Input 3 numbers: ").split(None, 2)]
except ValueError:
    print("Input error!")
else:
    s = 0
    for i in range(3):
        s += arr[i] if arr[i] % 5 == 0 else 0
    if s != 0:
        print(s)
    else:
        print("Error!")
finally:
    print("Done!")
