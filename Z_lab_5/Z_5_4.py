# Задание 4 лабораторная 5
# Вариант 1
# Збаразский С.С

import numpy as np
from numpy.random import default_rng


class Determinant():
    def main(self):
        rng = default_rng()
        matrix = rng.integers(100, high=200, size=(3, 3))
        print("Сгенерировання матрица:")
        self.PrintMatrix(matrix)

        return np.linalg.det(matrix)

    def PrintMatrix(self, matrix):
        print(matrix)


print("Детерминант матрицы:", Determinant().main())
