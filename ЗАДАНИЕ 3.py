while True:
    try:
        n = int(input("Введите количество элементов: "))
        break
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

s = []
for _ in range(n):
    while True:
        try:
            x = int(input("Введите элемент списка (целое число): "))
            break
        except ValueError:
            print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")
    s.append(x)

index=1
k=1000000000000000
for i in s:
    i = str(i)
    if i[0]=="-":
        i = i[1:]
    i= int(i)
    if i < k:
        k=i
        indexmin=index
    index+=1

indexotr=0
summ=0
for i in range(len(s)):
    if s[i]<0:
        indexotr=i
        break
for i in range(len(s)):
    if i > indexotr:
        s[i] = str(s[i])
        if s[i][0] == "-":
            s[i] = s[i][1:]
        s[i] = int(s[i])
        summ+=s[i]

print("Созданный список: ", *s)
print("Номер минимального числа по модулю в списке: ", indexmin)
print("Сумма модулей элемента списка, расположенных после первого отрицательного элемента: ",summ)
