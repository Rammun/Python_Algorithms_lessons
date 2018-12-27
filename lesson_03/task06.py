# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
min_item = 1
max_item = 50
array = [random.randint(min_item, max_item) for _ in range(SIZE)]

print(array)

max_i = 0
min_i = 0

for i in range(len(array)):
    if array[i] < array[min_i]:
        min_i = i
    if array[i] > array[max_i]:
        max_i = i

if min_i > max_i:
    min_i, max_i = max_i, min_i

summ = 0
for i in range(min_i + 1, max_i):
    summ += array[i]

print(f"Сумма чисел между числами {array[min_i]} и {array[max_i]} равняется {summ}")