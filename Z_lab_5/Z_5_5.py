# Задание 5 лабораторная 5
# Вариант 1
# Збаразский С.С

import numpy as np
from numpy.random import default_rng

class SumMatrix():
  def main(self):
    rng = default_rng()
    first = rng.integers(100, high=200, size=(3, 3))
    print("Первая матрица:")
    self.PrintMatrix(first)

    second = rng.integers(0, high=6, size=(3, 3))
    print("Вторая матрица:")
    self.PrintMatrix(second)

    exp_result = self.SumMatrix(first, second)
    print("Результирующая матрица:")
    self.PrintMatrix(exp_result)

    return np.linalg.det(exp_result)

  def SumMatrix(self, matrixA, matrixB):
    return matrixA + matrixB

  def PrintMatrix(self, matrix):
    print(matrix)

print("Детерминант результирующей матрицы:", SumMatrix().main())
