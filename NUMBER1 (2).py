while True:
    try:
        A = int(input("Введите значение A : "))
        break
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

while True:
    try:
        B = int(input("Введите значение B : "))
        break
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

while True:
    try:
        C = int(input("Введите значение C : "))
        break
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

while True:
    try:
        D = int(input("Введите значение D : "))
        break
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

def mean(X, Y):
    amean = (X+Y)/2
    gmean = (X*Y)**0.5
    return [amean, gmean]


print('Среднее алгебраическое А и В: ', mean(A,B)[0], '||', 'Среднее геометрическое A и В: ', mean(A,B)[1])
print('Среднее алгебраическое А и C: ', mean(A,C)[0], '||', 'Среднее геометрическое A и C: ', mean(A,C)[1])
print('Среднее алгебраическое А и D: ', mean(A,D)[0], '||', 'Среднее геометрическое A и D: ', mean(A,D)[1])
