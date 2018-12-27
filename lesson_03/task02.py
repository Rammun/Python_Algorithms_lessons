# 2. Во втором массиве сохранить индексы четных элементов первого массива. 
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй 
# массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация 
# начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 10
min_item = 1
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(SIZE)]

print(array)

result = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        result.append(i)

if len(result) == 0:
    print("В исходном массиве нет четных чисел.")
else:
    print(result)