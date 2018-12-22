# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

while True:
	n = int(input("Количество элементов (n): "))

	if(n == 0):
		sum = 0
	else:
		sum = 1
	count = 1
	current_numeral = 1
	while count < n:
		current_numeral *= -0.5
		sum += current_numeral
		count += 1

	print (f"Сумма ряда равна: {sum}")
	print(f"Контрольная сумма {(1.0 - (-0.5)**n) / 1.5}")


