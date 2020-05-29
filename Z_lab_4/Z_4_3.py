# Задание 3 лабораторная 4
# Вариант 1
# Збаразский С.С

from random import randint

# массив
weather = ["Ох и погодка", "Холодно", "ОЧень холодно", "Тепло как ни как", "Солнешко"]
text = input("Введите текст: ")
text = text + ": _"
rand_index = randint(0, len(weather))
text = text.replace("_", weather[rand_index])
print(text)
