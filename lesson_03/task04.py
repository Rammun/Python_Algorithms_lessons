# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
min_item = 1
max_item = 5
array = [random.randint(min_item, max_item) for _ in range(SIZE)]

print(array)

counts = {}
for num in array:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

max_item_key = None
for key, val in counts.items():
    if(max_item_key == None or counts[max_item_key] < val):
        max_item_key = key

print(f"Число {max_item_key} встречается {counts[max_item_key]} раз.")

