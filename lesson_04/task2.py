# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
#  a) Без использования «Решета Эратосфена»
#  б) Используя алгоритм «Решето Эратосфена»

import cProfile

def prime_number(i):	
	count = 1
	primes = [2]
	current_number = 3

	while count < i:
		if current_number > 10 and current_number % 10 == 5:
			pass
		else:
			for j in primes:
				if j * j - 1 > current_number:
					primes.append(current_number)
					count += 1
					break
				if (current_number % j == 0):
					break
			else:
				primes.append(current_number)
				count += 1

		current_number += 2

	return primes[-1]

# 1000 loops, best of 5: 8.85 usec per loop  - 10
# 1000 loops, best of 5: 268 usec per loop   - 100
# 1000 loops, best of 5: 7.04 msec per loop  - 1000
# 1000 loops, best of 5: 223 msec per loop   - 10000

# cProfile.run('prime_number(1000)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.041    0.041    <string>:1(<module>)
#     1    0.040    0.040    0.041    0.041    task2.py:7(prime_number)
#     1    0.000    0.000    0.041    0.041    {built-in method builtins.exec}
#   999    0.000    0.000    0.000    0.000    {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000    {method 'disable' of '_lsprof.Profiler' objects}

def sieve(i):
	n = 100000
	numbers = list(range(n + 1))
	numbers[1] = 0
	primes = []

	index = 2
	while index <= n:
		if numbers[index] != 0:
			primes.append(numbers[index])
			for j in range(index, n + 1, index):
				numbers[j] = 0
		index += 1
	return primes[i - 1]

# 1000 loops, best of 5: 54.6 msec per loop  - 10
# 1000 loops, best of 5: 53.7 msec per loop  - 100
# 1000 loops, best of 5: 54.9 msec per loop  - 1000
# Выход за пределы массива                   - 10000

# cProfile.run('sieve(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.002    0.002    0.109    0.109  <string>:1(<module>)
#     1    0.106    0.106    0.107    0.107  task2.py:44(sieve)
#     1    0.000    0.000    0.109    0.109  {built-in method builtins.exec}
#  9592    0.001    0.000    0.001    0.000  {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000  {method 'disable' of '_lsprof.Profiler' objects}

def test_prime_number(func):
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
	for i in range(1, len(primes)):
		result = func(i)
		assert result == primes[i - 1]
		print (f"Ok i = {i}, result = {result}")

# test_prime_number(prime_number)
# test_prime_number(sieve)

# Вывод:
# Функция prime_number имеет сложность О(n**2), чем большее число подается на вход, тем дольше в геометрической прогрессии будет выполняться алгоритм.
# Функция sieve имеет сложность O(1). Независимо от входных данных, метод будет выполняться примерно за одно и тоже время, которое тратится на создание списка простых чисел.
# Но алгоритм затратен ресурсами памяти на создание первоначального списка при больших входящих числах.
