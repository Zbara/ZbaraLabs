# Задание 3 лабораторная 5
# Вариант 1
# Збаразский С.С

import numpy as np

a = np.array([i for i in range(1, 100+1, 1)], int)
print("Массив:")
print(str(a))
a = a * a
print("Квадратный массив:")
print(str(a))
a = a.reshape((10, 10))
print("Матрица 10x10:")
print(str(a))
