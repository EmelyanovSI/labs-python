# Emelyanov SI Lab1

# 12. Выведите на экран квадрат из нулей и единиц, причем нули находятся только на диагонали квадрата.
# Всего в квадрате сто цифр.

for i in range(10):
    for j in range(10):
        if i is j:
            print('0', end=' ')
        else:
            print('1', end=' ')
    print(end='\n')
# Lab1 end
