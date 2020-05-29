# Задание 1 лабораторная 3
# Вариант 1
# Збаразский С.С


import random
count = 0

random_list = [random.randint(-10, 50) for i in range(10)]
print(random_list)
for i in range(10):
    if abs(random_list[i]) < 2:
        print(random_list[i], "\n", "*")
        count += 1
    else:
        print(random_list[i])
print("\n", count)
