#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ =="__main__":
    my1 = input("Введите символы в строку 1: ")
    my2 = input("Введите символы в строку 2: ")

    total = set(my1).intersection(set(my2))

    if total:
        print("Общие символы: ",total)
    else:
        print("Общих символов нет.")
