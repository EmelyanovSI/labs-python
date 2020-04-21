# EmelyanovSI lab3

# 6. Вывести ряд чисел: десять десяток, девять девяток, восемь восьмерок, ... , одну единицу.
# Найти сумму всех этих чисел.

try:
    s = 0
    kol = 10
    while kol != 0:
        for i in range(kol):
            print(kol, end=' ')
        print()
        s += pow(kol, 2)
        kol -= 1
except IndexError:
    print("Output error!")
else:
    print("Total amount: " + str(s))
finally:
    print("Done!")
