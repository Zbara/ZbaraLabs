# Задание 8 лабораторная 3
# Вариант 1
# Збаразский С.С

# улица, номер дома и номер квартиры.
stack = [["Чехова", 34, 2], ["Тираспольская", 434, 8], ["Екатеринаская", 22, 16], ["Тираспольская", 343, 2]]

new_stack = []
for st, home, k in stack:
    if home % 2 == 0:
        new_stack.append([st, home, k])

stack = new_stack
for i in stack:
    print(i)

count = 0
for st, home, k in stack:
    if st == "Тираспольская":
        count += 1

print(count)
