# Задание 8 лабораторная 4
# Вариант 1
# Збаразский С.С


text = input("Введите текст: ")
print("Текст: ", text)
print("Шифрувание: ")
encryption = ""
for x in range(len(text) - 1, -1, -1):
    encryption += text[x]
print(encryption)
print("Дешифровки: ")
decryption = ""
for x in range(len(text) - 1, -1, -1):
    decryption += encryption[x]
print(decryption)
