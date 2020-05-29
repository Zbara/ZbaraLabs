# Задание 10 лабораторная 3
# Вариант 1
# Збаразский С.С

old_dict = {"Пес": "Dog", "Кошка": "Cat"}

new_dict = dict([(value, key) for key, value in old_dict.items()])

for i in old_dict:
    print(i, " :  ", old_dict[i])
print()

for i in new_dict:
    print(i, " :  ", new_dict[i])