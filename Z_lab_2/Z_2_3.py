# Задание 2 лабораторная 2
# Вариант 1
# Збаразский С.С

sum = 0
for i in range(1, 3):
    if i % 2 != 0:
        sum += i - i ** 2
    else:
        sum += i / 2 - i ** 3

print(sum)
