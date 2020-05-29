# Задание 4 лабораторная 2
# Вариант 1
# Збаразский С.С

n = int(input("Введите натуральное число: "))
sum = 0

for x in range(1, n + 1):
    if x % 3 == 0:
        sum += x**2
    elif x % 3 == 1:
        sum += x

    else:
        sum += x/3
print(sum)
