#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ =="__main__":
    diction = {'а','А','е','Е','ё','Ё','и','И','о','О','у','У','э','Э','ю','Ю','я','Я','ы','Ы'}
    mytext = input("Введите строку: ")
    count = 0
    for char in mytext:
        if char in diction:
            count += 1

    print(f"Количество гласных в ведёной строке: {count}")