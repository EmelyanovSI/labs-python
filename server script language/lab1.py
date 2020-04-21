# EmelyanovSI lab1

# 6. Пользователь вводит время в минутах и расстояние в километрах. Найдите скорость в м/c.

print("v=s/t")
try:
    while True:
        print("Input time(minutes):")
        t = float(input("t = "))
        if t > 0:
            break
        else:
            print("Try again!")
    print("Input distance(km):")
    s = float(input("s = "))
except ValueError:
    print("Input error!")
else:
    v = (abs(s) * 1000) / (t * 60)
    print("Ok, the result is:")
    print("v=" + str(v) + "m/s")
finally:
    print("Done!")
