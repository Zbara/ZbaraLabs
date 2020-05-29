# Задание 6 лабораторная 2
# Вариант 1
# Збаразский С.С

import math

sum = 0
a = -1
b = 2

while a <= b:
    if a < 0:
        sum += math.pi + 3 * a**3
        a += 0.1
        print("Сумма < 0: ", sum)
    if a >= 0:
        sum += math.cos((2.1 * a + math.exp(a)) ** (1/3))
        a += 0.1
        print("Сумма >= 0: ", sum)


