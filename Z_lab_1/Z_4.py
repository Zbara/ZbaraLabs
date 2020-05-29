# Задание 4 лабораторная 1
# Вариант 1
# Збаразский С.С

import math
x = 10
a = 35
b = 3
c = 4

f1 = 0.87 * ((((a * x**2 - b) + c) * x - b) / (x - 1 + ((1 + b) / (1 - a))))
print("F1 = ", f1)

f2 = (math.log(math.sqrt(x)) + x**(math.log(math.sqrt(x))) - math.sin(x)) / -1
print("F2 = ", f2)