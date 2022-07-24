# 3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]

import numbers


num = int(input('Введите натуральное число: '))
def simpleDividers(n):
    answer=[]
    d=2
    while d*d <=n:
        if n%d==0:
            answer.append(d)
            n//=d
        else:
            d+=1
    if n>1:
        answer.append(n)
    return answer

print(simpleDividers(num))