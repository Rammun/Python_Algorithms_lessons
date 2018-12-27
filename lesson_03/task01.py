# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9

import random

SIZE = 10
min_item = 2
max_item = 99
array = [random.randint(min_item, max_item) for _ in range(SIZE)]

print(array)

count = 0
for num in array:
    for divisor in range(2,10):
        if num % divisor == 0:
            count += 1
            break

print(count)