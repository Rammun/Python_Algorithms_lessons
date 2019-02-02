# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
# и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random

def bubble_sort(source):
    array = source.copy()

    n = 1
    while n < len(array):
        is_changed = False
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_changed = True

        if(not is_changed):
            break
        n += 1

    return array


count = 10
array = [random.randint(-100, 99) for i in range(count)]
print(array)
print()

result = bubble_sort(array)
print(result)
