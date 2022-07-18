# #1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

def RealNumber():
    try:
        number=input('Введите вещественное число: ')
        if float(number)==True:
            return float(number)
        else:
            number=number.replace('.','')
            return float(number)
    except:
        print('Введите вещественное число, в качестве разделителя использовать ".": ')
        return RealNumber()
def SumElements(number):
    result = 0
    while number > 0:
        result = result +number% 10
        number = number // 10
    return result
inputNumber=RealNumber()
print(f'Сумма элементов вещественного числа равна {round(SumElements(inputNumber))}')