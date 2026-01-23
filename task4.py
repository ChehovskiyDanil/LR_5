#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ =="__main__":
    numbers = {
        1:"один",
        2:"два",
        3:"три",
        4:"четыре",
        5:"пять",
    }
    print("Начальные данные: ")
    for first, second in numbers.items():
        print(f"Ключ {first}: его значение {second} ")

    swap_numbers = dict(zip(numbers.values(), numbers.keys()))
    print("\nПеревёрнутые данные: ")
    for first, second in swap_numbers.items():
        print(f"Ключ {first}: его значение {second} ")