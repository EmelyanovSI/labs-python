# EmelyanovSI lab5

# 6. Напишите простую функцию, которая удаляет точки и квоты из текста ввода.
# Подпись функции: def remove_dots_quotas (текст)


def remove_dots_quotas(s):
    quotas = "!@#$%^&*()_+-=,./<>?:{};[]'`~|/\"\\"
    for i in range(len(quotas)):
        s = s.replace(quotas[i], '')
    return s


try:
    string = input("Input string: ")
except ValueError:
    print("Input error!")
else:
    string = remove_dots_quotas(string)
    print(string)
finally:
    print("Done!")
