l = input('Введите текст:').split()
s=l.copy()
print(s)
for i in range(len(s)):
    flag = True
    if not s[i][-1] in "йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnm" and not s[i][-1] in "1234567890":
        s[i] = s[i][0:-1]
    for j in range(len(s[i])):
        if not s[i][j] in "йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnm":
            flag = False
    if flag == False:
        while flag == False:
            print('Слово', s[i], 'введено не правильно.')
            s[i] = input('Введите данное слово без ошибок: ')
            newS = s[i]
            k = 0
            for x in range(len(newS)):
                if newS[x] in "йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnm":
                    k += 1
            if k == len(newS): flag = True

k = 0
for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j] == "а" or s[i][j] == "a" or s[i][j] == "А" or s[i][j] == "A":
            k += 1
print("Созданный список: ", *l)
print("Измененный список: ", *s)
print("Количество букв 'А' в тексте: ", k)

