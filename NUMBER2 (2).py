import math
def pr(s):
    while True:
        try:
            r1 = float(input("Введите значение {}: ".format(s)))
            if r1 > 0:
                return r1
                break
            else:
                print('Введите значение {} большее нуля: '.format(s))
                continue
        except ValueError:
            print("Вы ввели некорректное значение. Пожалуйста, введите число правильно.")

def pr2(s):
    while True:
        try:
            fi1 = int(input("Введите значение {} : ".format(s)))
            return fi1
            break
        except ValueError:
            print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

r1=pr('R1')
r2=pr('R2')
fi1=pr2('φ1')
fi2=pr2('φ2')

def d(r1, r2, fi1, fi2):
    return (r1**2 + r2**2 - 2 * r1 * r2 * math.cos((fi1-fi2)))**0.5

print('Длина отрезка на плоскости при заданных полярных координатах: ', d(r1, r2, fi1, fi2))