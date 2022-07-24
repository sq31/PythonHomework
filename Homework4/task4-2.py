# 2- Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.
# Посмотрели, что такое множество? Вот здесь его не используйте.

import numbers
from random import randint
numbers = [randint(0, 10) for _ in range(10)]
print(numbers)


def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)
    return list_of_unique_numbers


print(get_unique_numbers(numbers))
