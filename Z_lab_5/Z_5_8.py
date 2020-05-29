# Задание 8 лабораторная 5
# Вариант 1
# Збаразский С.С

import numpy as np

fruits = np.array(
    ['Абрикос', 'Айва', 'Виноград', 'Вишня', 'Груша', 'Земляника', 'Крыжовник', 'Малина', 'Персик', 'Слива',
     'Черная смородина', 'Черешня', 'Шиповник', 'Яблоко'])
vitamin_amounts = np.array([
    [1.6, 0.03, 0.06, 0.07, 6, 570],
    [0.2, 0.03, 0.03, 0.02, 115, 415],
    [0.01, 0.01, 0.01, 0.06, 4, 300],
    [0.7, 0.03, 0.03, 0.04, 15, 370],
    [0.01, 0.02, 0.03, 0.01, 5, 120],
    [0.03, 0.03, 0.05, 0.03, 60, 200],
    [0.2, 0.01, 0.02, 0.25, 32, 250],
    [0.02, 0.02, 0.05, 0.06, 25, 180],
    [0.05, 0.04, 0.01, 0.07, 15, 350],
    [0.07, 0.06, 0.04, 0.06, 5, 312],
    [0.1, 0.02, 0.02, 0.03, 200, 500],
    [0.15, 0.01, 0.01, 0.04, 15, 95],
    [0.25, 0.03, 0.06, 0.05, 300, 600],
    [0.03, 0.01, 0.03, 0.03, 5, 250]
])
vitamins = np.array(['А', 'В1', 'В2', 'РР', 'С', 'Р'])

indexed_vitamins = np.rec.fromarrays((vitamins, range(1, len(vitamins) + 1)))
print(indexed_vitamins)

vitamin_indx = int(input(("Выберите витамин (цифра): "))) - 1
max_vitamins_indx = np.argmax(vitamin_amounts, axis=0)
print("Содержание выбранного витамина максимально в:", fruits[max_vitamins_indx[vitamin_indx]])

vitamin_indx = int(input(("Выберите витамин (цифра): "))) - 1
amount = float(input(("Задайте желаемое количество: ")))
for index, el in np.ndenumerate(vitamin_amounts):
    (r, c) = index
    if c == vitamin_indx:
        count = amount / el
        print(fruits[r], " - Масса: %.2f" % count)

print("Задайте набор фруктов")
vitamins_sum = np.zeros((len(vitamins),))
for i in range(len(fruits)):
    count = 0
    try:
        count = float(input("%s " % fruits[i]))
    except ValueError as identifier:
        pass

    vitamins_sum = vitamins_sum + vitamin_amounts[i] * count

records = np.rec.fromarrays((vitamins, vitamins_sum), names=('vitamins', 'amount'))
np.set_printoptions(suppress=True)
print('Содержание витаминов в наборе', records)
