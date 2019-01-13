# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.

import cProfile

# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def variant_1(number):
	even_count = 0
	odd_count = 0
	while number != 0:
		numeral = number % 10
		if(numeral % 2 == 0):
			even_count += 1
		else:
			odd_count += 1
		number = number // 10

	return (even_count, odd_count)

# 100000 loops, best of 5: 2.29 usec per loop   - 123456 (6 цифр)
# 100000 loops, best of 5: 5.05 usec per loop   - 123456789012 (12 цифр)
# 100000 loops, best of 5: 9.33 usec per loop  - 123456789012345678 (18 цифр)
# 100000 loops, best of 5: 12.8 usec per loop  - 123456789012345678901234 (24 цифр)

# cProfile.run('variant_1(123456789012345678901234)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000  <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000  task1.py:5(variant_1)
#     1    0.000    0.000    0.000    0.000  {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000  {method 'disable' of '_lsprof.Profiler' objects}

def variant_2(number):
	even_count = 0
	odd_count = 0
	number = str(number)
	for n in number:
		if(int(n) in [1, 3, 5, 7, 9]):
			odd_count += 1
	for n in number:
		if(int(n) in [2, 4, 6, 8, 0]):
			even_count += 1

	return (even_count, odd_count)

# Оптимистичный вариант
# 100000 loops, best of 5: 5.45 usec per loop  - 121212 (6 цифр)
# 100000 loops, best of 5: 9.96 usec per loop  - 121212121212 (12 цифр)
# 100000 loops, best of 5: 19.7 usec per loop  - 121212121212121212121212 (24 цифр)

#Пессимистичный вариант
# 100000 loops, best of 5: 6.92 usec per loop  - 909090 (6 цифр)
# 100000 loops, best of 5: 12.8 usec per loop  - 909090909090 (12 цифр)
# 100000 loops, best of 5: 25.3 usec per loop  - 909090909090909090909090 (24 цифр)

# Усредненный выриант
# 100000 loops, best of 5: 6.31 usec per loop  - 123456 (6 цифр)
# 100000 loops, best of 5: 12.4 usec per loop  - 123456789012 (12 цифр)
# 100000 loops, best of 5: 20.0 usec per loop  - 123456789012345678 (18 цифр)
# 100000 loops, best of 5: 29.5 usec per loop  - 123456789012345678901234 (24 цифр)

# cProfile.run('variant_2(123456789012345678901234)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    1    0.000    0.000    0.000    0.000   <string>:1(<module>)
#    1    0.000    0.000    0.000    0.000   task1.py:30(variant_2)
#    1    0.000    0.000    0.000    0.000   {built-in method builtins.exec}
#    1    0.000    0.000    0.000    0.000   {method 'disable' of '_lsprof.Profiler' objects}


# Вывод:
#
# Алгоритм функции variant_1 имеет сложность O(n). По замеру времени заметна линейная зависимость
#     6 цифр - 2.29   12 цифр - (2.29 * 2) ~ 5.05   18 цифр - (2.29 * 3) ~ 9.33   24 цифры - (5.05 * 2 или 2.29 * 4) ~ 12.8
#
# Алгоритм функции variant_2 в общем виде так же имеет сложность O(n). Но не оптимален т.к. есть два цикла по последовательности (О(2n)) 
# и внутри цикла есть поиск в массиве константной длины 5, т.е. реальная сложность алгоритма О(2 * 5 * n) = О(10n).
# Алгоритм может показать сложность О(6n) при условии, что число состоит только из [1, 2], в этом случае исключается 
# прохождение в одном из циклов по всему массиву в поиске совпадения четного или нечетного числа.
# По замеру времени видно, что пессимистичный вариант сложнее оптимистичного и по времени выполнения близок к усредненному варианту.
# Пессиместичный вариант, это тот случай когда сложность гарантировано O(10n), т.к. будет полное прохождение по всему массиву в двух циклах.
