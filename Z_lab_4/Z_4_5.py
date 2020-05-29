# Задание 5 лабораторная 4
# Вариант 1
# Збаразский С.С

words = list()
print("Задайте строки:")
for i in range(1, 6):
    words.append(input('s%s. ' % i))

concat_str = words[0] + ' '
if words[3] != words[4]:
    concat_str += words[2]
else:
    concat_str += words[1]
print("Результат:", concat_str)
