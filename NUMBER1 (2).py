def error():
    print("Введено неправильное значение")

while True:
    try:
        A = float(input("Введите значение A : "))
        B = float(input("Введите значение B : "))
        C = float(input("Введите значение C : "))
        D = float(input("Введите значение D : "))
        break
    except:
        error()


def mean(X, Y):
    amean = (X+Y)/2
    gmean = (X*Y)**0.5
    return [amean, gmean]


print('Среднее алгебраическое А и В: ', mean(A,B)[0], '||', 'Среднее геометрическое A и В: ', mean(A,B)[1])
print('Среднее алгебраическое А и C: ', mean(A,C)[0], '||', 'Среднее геометрическое A и C: ', mean(A,C)[1])
print('Среднее алгебраическое А и D: ', mean(A,D)[0], '||', 'Среднее геометрическое A и D: ', mean(A,D)[1])
