# Задание 2 лабораторная 4
# Вариант 1
# Збаразский С.С

n = int(input("Введите количетсво: "))
result = ""
result += str(n) + " "
if n == 1:
    result += "негритенок"
    result += " пошел"
else:
    if n >= 2 and n <= 4:
        result += "негритенка"
    if n >= 5 and n <= 10:
        result += "негритят"
    result += " пошли"
print(result)
