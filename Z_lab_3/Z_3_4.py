# Задание 4 лабораторная 3
# Вариант 1
# Збаразский С.С

print("Введіть кількість кубиків у Ані та Бориса: ")
ann, boris = list(map(int, input().split()))
a = set()

b = set()
print("Введіть кольори які є у Ані: ")
for i in range(ann):
    a.add(int(input()))
print("")
print("Введіть кольори які є у Бориса: ")
for i in range(boris):
    b.add(int(input()))
print("Кількість співпадань у Ані: ")
print(len(a.intersection(b)))
print("Кольори які співпали: ")
print(*sorted(a.intersection(b)))

print("Скільки залишилось кольорів у Ані: ")
print(len(a.difference(b)))
print("Які залишилось кольори у Ані: ")
print(*sorted(a.difference(b)))

print("Скільки залишилось кольорів у Бориса: ")
print(len(b.difference(a)))
print("Які залишилось кольори у Бориса: ")
print(*sorted(b.difference(a)))