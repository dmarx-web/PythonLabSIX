import math

while True:
    try:
        r1 = float(input("Введите значение R1: "))
        if r1 > 0:
            break
        else:
            print('Введите значение R1 большее нуля: ')
            continue
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите число правильно.")

while True:
    try:
        r2 = float(input("Введите значение R2: "))
        if r2 > 0:
            break
        else:
            print('Введите значение R2 большее нуля: ')
            continue
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите число правильно.")

while True:
    try:
        fi1 = int(input("Введите значение φ1 : "))
        break
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

while True:
    try:
        fi2 = int(input("Введите значение φ2 : "))
        break
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

def d(r1, r2, fi1, fi2):
    return (r1**2 + r2**2 - 2 * r1 * r2 * math.cos((fi1-fi2)))**0.5

print('Длина отрезка на плоскости при заданных полярных координатах: ', d(r1, r2, fi1, fi2))

