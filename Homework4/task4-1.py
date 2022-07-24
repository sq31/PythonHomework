# 1- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi,
# а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.
# Пример:
# - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

from itertools import count
from unicodedata import decimal

import math
d = decimal(input('Введите точность округления для числа Пи: '))
def RoundPi(d):
    count = 0
    while 10**(-10) <= d <= 10**(-1):
        count += 1
        d *= 10
    return f'При указанной точности число Пи(Pi)= {(round(math.pi,d))}'


print(RoundPi(d))
