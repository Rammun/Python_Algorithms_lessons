# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
min_item = -100
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(SIZE)]

print(array)

max_negative_i = None
for i in range(len(array)):
    if array[i] < 0 and (max_negative_i == None or  array[i] > array[max_negative_i]):
        max_negative_i = i

if(max_negative_i == None):
    print("Нет отрицательных чисел.")
else:
    print(f"index: {max_negative_i}; value: {array[max_negative_i]}")
