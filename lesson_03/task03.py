# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
min_item = 1
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(SIZE)]

print(array)

max_i = 0
min_i = 0

for i in range(len(array)):
    if array[i] < array[min_i]:
        min_i = i
    if array[i] > array[max_i]:
        max_i = i

array[min_i], array[max_i] = array[max_i], array[min_i]

print(array)