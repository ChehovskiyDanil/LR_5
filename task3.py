#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ =="__main__":
    school = {
        "1А":20,
        "1Б": 19,
        "2А": 21,
        "3Б": 17,
        "5А": 23,
        "7А": 20,
        "7Б": 17,
    }
    print("Начальные данные о классах: ")
    for school_class, students in school.items():
        print(f"Класс {school_class}: {students} учеников")

    school['7А'] = 19
    print("\nа) В 7А классе изменилось количество учащихся: ", school['7А'])

    school['5Б'] = 19
    print("б) В школе появился новый класс 5Б: ", school['5Б'])

    del school['3Б']
    print("в) Класс 3Б был расформирован")

    print("\nОбновленные данные о классах: ")
    for school_class, students in school.items():
        print(f"Класс {school_class}: {students} учеников")

    total_students = sum(school.values())
    print(f"\nОбщее количество учащихся в школе: {total_students} учеников")