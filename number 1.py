import random


def max_element_in_matrix(matrix):
    max_element_in_row = []

    for row in range(len(matrix)):
        max_element = {'digit': -1000000, 'row': 0, 'col': 0}
        for col in range(len(matrix[row])):

            if matrix[row][col] > max_element['digit']:
                max_element['digit'] = matrix[row][col]
                max_element['row'] = row
                max_element['col'] = col

        max_element_in_row.append(max_element)

    min_element = {'digit': 1000000, 'row': 0, 'col': 0}

    for dicti in max_element_in_row:

        if dicti['digit'] < min_element['digit']:
            min_element['digit'] = dicti['digit']
            min_element['row'] = dicti['row']
            min_element['col'] = dicti['col']

    return min_element


while True:
    try:
        number_elements = int(input("Введите количество строк: "))
        if number_elements >= 0:
            break
        else:
            print("Ошибка: Введено отрицательное число. Попробуйте снова.")
        break
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

while True:
    try:
        number_of_rows = int(input("Введите количество элементов в строке: "))
        if number_of_rows >= 0:
            break
        else:
            print("Ошибка: Введено отрицательное число. Попробуйте снова.")
        break
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

matrix = [[random.randint(1, 100) for j in range(number_of_rows)] for i in range(number_elements)]

answer = max_element_in_matrix(matrix)
print('Матрица:')
print(*matrix, sep='\n')
print('Минимальный элемент среди максимальных элемeнтов в строках:', answer['digit'])
print('Номер строки элемента: ', answer['row'] + 1)
print('Номер столбца элемента: ', answer['col'] + 1)