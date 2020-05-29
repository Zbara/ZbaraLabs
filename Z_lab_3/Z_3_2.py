# Задание 2 лабораторная 3
# Вариант 1
# Збаразский С.С

import random

count = 0
random_list = [random.randint(0, 10) for i in range(10)]
print(random_list, "\n\n")
random_list1 = [random.randint(0, 10) for i in range(10)]
print(random_list1)
for i in random_list:
    for j in random_list1:
        if i == j and i % 3 == 0 and j % 3 == 0:
            count += 1
print("\n", count)




