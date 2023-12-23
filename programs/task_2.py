#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), c с помощью полученного объекта
# dict_items создайте новый словарь, "обратный" исходному,
# т. е. ключами являются строки, а значениями – числа.

if __name__ == '__main__':
    original_dict = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten'
    }

    print("Original dictionary: ")
    print(original_dict)

    swapped = {v: k for k, v in original_dict.items()}

    print("\nReversed dictionary: ")
    print(swapped)
