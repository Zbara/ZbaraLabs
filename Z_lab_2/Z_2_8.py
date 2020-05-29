# Задание 8 лабораторная 2
# Вариант 1
# Збаразский С.С

import math

n = 2
i = n ** (-2)
sumT = (math.pi ** 2)/6
e = 10 ** (-4)
sum = i

while abs(i) < e:
    sum += i
    n += 1
    i = n ** (-2)

print("Сумма = ", sum)
print("Сумма T = ", sumT)
