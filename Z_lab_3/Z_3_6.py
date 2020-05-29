# Задание 6 лабораторная 3
# Вариант 1
# Збаразский С.С

n = int(input('Введите n: '))
k = int(input('Введите k: '))
x_days = set()
for i in range(k):
    a, b = [int(x) for x in input().split()]
    for day in range(a - 1, n, b):
        if (day + 1) % 6 and (day + 1) % 7:
            x_days.add(day)
print(x_days)
print(len(x_days))

