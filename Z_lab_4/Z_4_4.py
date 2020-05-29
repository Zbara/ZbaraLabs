# Задание 4 лабораторная 4
# Вариант 1
# Збаразский С.С

words = list()
print("Задайте 3 слова для сортировки:")
for i in range(1, 4):
    words.append(input('%s. ' % i))

sorted_words = sorted(words, key=len, reverse=True)
print("Отсортированные слова:", sorted_words)
