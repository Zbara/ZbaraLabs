# Задание 7 лабораторная 3
# Вариант 1
# Збаразский С.С

words = input('Введите предложение: ').split(' ')
y_word_index = int(input('Введите индекс у: ')) - 1
y_word = words[y_word_index]
actions_count = int(2 * sum(map(len, words)))
for i in range(min(len(words), actions_count)):
    if i == y_word_index:
        continue
    if y_word.find(words[i]) != -1:
        print(words[i], 'подстрока', y_word)
        break
