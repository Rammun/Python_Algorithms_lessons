# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

while True:
	number = int(input("Введите число: "))

	even_count = 0
	odd_count = 0
	while number != 0:
		numeral = number % 10
		if(numeral % 2 == 0):
			even_count += 1
		else:
			odd_count += 1
		number = number // 10

	print(f"Кол-во четных цифр в числе: {even_count}")
	print(f"Кол-во нечетных цифр в числе: {odd_count}")
	print("")