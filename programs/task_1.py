#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Cоздайте словарь, связав его с переменной school,
# и наполните данными, которые бы отражали количество учащихся
# в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему:
# а) в одном из классов изменилось количество учащихся,
# б) в школе появился новый класс,
# с) в школе был расформирован (удален) другой класс.
# Вычислите общее количество учащихся в школе


if __name__ == '__main__':
    school = {
        '1a': 30,
        '1б': 30,
        '1в': 28,
        '2a': 28,
        '2б': 26,
        '3a': 26,
        '3б': 31,
        }
    print("School: ")
    print(school)

    # а) в одном из классов изменилось количество учащихся
    change_class = input("Enter the class name... ")
    change_num = int(input("Enter new number of student... "))

    school[change_class] = change_num
    print("School: ")
    print(school)

    # б) в школе появился новый класс
    new_class = input("Enter the new class name... ")
    new_num = int(input("Enter the number of student... "))

    school[new_class] = new_num
    print("School: ")
    print(school)

    # с) в школе был расформирован (удален) другой класс
    del_class = input("Enter the name class to delete it: ")
    del school[del_class]
    print("School: ")
    print(school)

    total = sum(school.values())
    print(f"The tottal number of student is {total}.")
