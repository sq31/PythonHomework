# 2 - Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


from random import randint as rd

size = int(input('Введите колчество элементов: '))
rnd_list = [rd(1, 9) for _ in range(size)]
print(rnd_list)

def sum_of_num(num_list: list) -> list:
    result = []
    index = 0
    lst_index = len(num_list) - 1
    while lst_index - index >= 0:
        result.append(num_list[index] * num_list[lst_index])
        index += 1
        lst_index -= 1
    return result

print(sum_of_num(rnd_list))
