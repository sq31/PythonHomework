# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = 0
while num < 1:
    try:
        num = int(input("Введите натуральное число: "))
    except Exception as error:
        print(error)

def fibonacci_plus(num: int) -> list:
    numbers_plus = [0, 1]
    for i in range(1, num):
        numbers_plus.append(numbers_plus[-1] + numbers_plus[-2])
    return numbers_plus

def fibonacci_minus(num: int) -> list:
    numbers_minus = [0, 1]
    for i in range(1, num):
        numbers_minus.append(numbers_minus[-2] - numbers_minus[-1])
    return numbers_minus

print(fibonacci_minus(num)[::-1] + fibonacci_plus(num)[1:])
