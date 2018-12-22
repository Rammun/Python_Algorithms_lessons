# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

while True:
	number = int(input("Введите число: "))

	result = 0
	while number != 0:
		numeral = number % 10
		result = result * 10 + numeral
		number = number // 10

	print(f"Обратное число: {result}")
	print("")