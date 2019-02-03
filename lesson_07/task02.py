# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

def merge_sort(array):
    length = len(array)
    if length < 2:
        return array

    middle_index = length // 2
    left = merge_sort(array[:middle_index])
    right = merge_sort(array[middle_index:])

    return merge(left, right)

count = 10
# source = [random.uniform(0, 50) for i in range(count) if i != 50]
source = []
for i in range(count):
    source.append(50)
    while source[i] == 50:
        source[i] = random.uniform(0, 50)

result = merge_sort(source)

print(source)
print()
print(result)