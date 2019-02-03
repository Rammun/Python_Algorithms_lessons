# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках

import random

def new_part(i, array):
    index = random.choice(array)

    lesser_part = [item for item in array if item < index]
    if len(lesser_part) > i:
        return new_part(i, lesser_part)
    i -= len(lesser_part)

    count = array.count(index)
    if count > i:
        return index
    i -= count

    greater_part = [item for item in array if item > index]
    return new_part(i, greater_part)

def get_median(array):
    length = len(array)
    
    if length % 2:
        return new_part(length // 2, array)
    else:
        left  = new_part((length - 1) // 2, array)
        right = new_part((length + 1) // 2, array)
        return (left + right) / 2

count = 11
source = [random.randint(0, 100) for i in range(count)]
print(source)
print(get_median(source))

# t = sorted(source)
# print(t[5])
