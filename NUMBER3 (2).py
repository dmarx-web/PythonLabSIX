word_list = input('Введите текст: ').split()


for index_word in range(len(word_list)):
    flag = True

    if not word_list[index_word][-1].isalpha() and not word_list[index_word][-1].isdigit():
        word_list[index_word] = word_list[index_word][0:-1]

    for index_alpha in range(len(word_list[index_word])):
        if not word_list[index_word][index_alpha].isalpha():
            flag = False

    if flag == False:
        while flag == False:
            print('Слово', word_list[index_word], 'введено не правильно.')
            word_list[index_word] = input('Введите данное слово без ошибок: ')
            new_word = word_list[index_word]
            count = 0
            for index in range(len(new_word)):
                if new_word[index].isalpha():
                    count += 1
            if count == len(new_word): flag = True

string = ''

for word in word_list:
    string += word
    string += ' '

while True:
    try:
        itoe = int(input("Введите элемент i: "))
        break
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

while True:
    try:
        jtoe = int(input("Введите элемент j (j>i): "))
        if jtoe > itoe:
            break
        else:
            print('Введите значение j большее i: ')
            continue
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")


def palindrom(string, itoe, jtoe):
    if string[itoe-1:jtoe-1] == string[itoe:jtoe][::-1]:
        return True
    else:
        return False

ans = palindrom(string, itoe, jtoe)

if ans == True: print('Данный фрагмент является палиндромом.')
else: print('Данный фрагмент не является палиндромом.')

