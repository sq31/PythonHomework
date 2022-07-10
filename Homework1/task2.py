# 2- Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

res = 0
print('x y z   Результат')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            res = (not(x or y or z) == (not x and not y and not z))
            print(x, y, z, '=', res)