# Задание 1 лабораторная 4
# Вариант 1
# Збаразский С.С

text = input('Введите текст ')
sentences_words_count = list(map(lambda s: len(list(filter(len, s.split(' ')))), filter(len, text.split('.'))))
print('Количество слов ', *sentences_words_count)

