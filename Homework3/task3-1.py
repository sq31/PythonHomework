# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def numbers(collection):
    sum = 0
    for i in range(1, len(collection)):
        if i % 2 != 0:
            sum += collection[i]
    return sum


collection_list = [1, 6, 3, 11, 4, 3]
print(f'Сумма элементов списка на четных позициях равна: {numbers(collection_list)}')
