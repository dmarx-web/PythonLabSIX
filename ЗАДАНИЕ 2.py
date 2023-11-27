t = input("Введите текст: ")
slovo = ""
text_list = []
for c in t:
    if c != " ":
        slovo += c
    else:
        text_list.append(slovo)
        slovo = ""
text_list.append(slovo)
s = text_list
print(s)

for i in range(len(s)):
    flag = True
    if not s[i][-1] in "йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnmЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM" and not s[i][-1] in "1234567890":
        s[i] = s[i][0:-1]

    for j in range(len(s[i])):
        if not s[i][j] in "йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnmЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM":
            flag = False

    if flag == False:
        while flag == False:
            print('Слово', s[i], 'введено не правильно.')
            s[i] = input('Введите данное слово без ошибок: ')
            newS = s[i]
            k = 0
            for x in range(len(newS)):
                if newS[x] in "йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnmЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNM":
                    k += 1
            if k == len(newS): flag = True

k = 0

for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j] in "qwertyuiopasdfghjklzxcvbnm":
            k += 1

print("Созданный список: ", *t)
print("Измененный список: ", *s)
print("Количество прописных латинских букв в тексте: ", k)
