# EmelyanovSI lab4

# 6. Дана строка.
# Определите, какой символ в ней встречается раньше: 'x' или 'w'.
# Если какого-то из символов нет, вывести сообщение об этом.

msg_x = "x appears earlier than w"
msg_w = "w appears earlier than x"
try:
    string = input("Input string: ")
    x = string.find('x')
    w = string.find('w')
except ValueError:
    print("Error!")
else:
    if x == -1:
        print("x wasn`t found!")
        print(msg_w)
    elif w == -1:
        print("w wasn`t found!")
        print(msg_x)
    elif x < w:
        print(msg_x)
    else:
        print(msg_w)
finally:
    print("Done!")
