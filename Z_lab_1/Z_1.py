# Задание 1 лабораторная 1
# Вариант 1
# Збаразский С.С

from math import pi


def main():
    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))
    conevol = 1 / 3 * pi * radius * 2 * height
    cylvol = pi * radius ** 2 * height
    spherevol = 3 / 4 * pi * radius ** 3
    print(" The volume of a cone", conevol)
    print(" The volume of a cylinder", cylvol)
    print(" The volume of a sphere", spherevol)


main()