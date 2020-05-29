# Задание 3 лабораторная 3
# Вариант 1
# Збаразский С.С

import random

random_list = [random.randint(0, 10) for i in range(10)]
print(random_list, "\n")


random_list1 = [random.randint(0, 10) for i in range(10)]
print(random_list1)


print(' '.join([str(i) for i in sorted(set(random_list) & set(random_list1)) if i % 2 == 0]))