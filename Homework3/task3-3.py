# 3 - Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564

a = [ ]             
n = 4   
for i in range (n):  
    new = float (input ('введите 4 числа в виде десятичных дробей через разделитель "."'))  
    a.append (new)      
print (a)
def MaxMin(list):
    for i in range(len(list)):
        list[i]=(round(list[i]%1,2)*100)
    Result=int(max(list)-min(list))
    return f'Разница между остатком дробей {int(max(list))} и {int(min(list))} = {Result}'
print(MaxMin(a))

