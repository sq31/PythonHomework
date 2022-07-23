# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def dec_to_bin(num: int) -> str:
    bin_num = ''
    while num > 0:
        bin_num += str(num % 2)
        num //= 2
    return bin_num[::-1]

print(dec_to_bin(255))
print(dec_to_bin(8))
print(dec_to_bin(111))