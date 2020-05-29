# Задание 5 лабораторная 2
# Вариант 1
# Збаразский С.С

import random

n = int(input("Введите натуральное число: "))
r = random.randint(0, 10)

max = min = r

for i in range(0, n):
    r = random.randint(0, 10)
    if max < r:
        max = r
    if min > r:
        min = r
    print(r)

print("Max: ", max, "\n", "Min: ", min)
print("Sum: ", max + min)
