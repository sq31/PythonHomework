# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

file = open('text_hw4', 'w', encoding='utf-8')
file.write('Одна4жды в студен6ую зимнюю пору я4 из лесу вышел б5ыл сиальный5 мороз.')
file.close()
file = open('text_hw4', 'r', encoding='utf-8')
data = file.read().split()
sort_list = []

for words in data:
    if words.isalpha():
        sort_list.append(words)
file.close()
print(' '.join(sort_list))
