# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

while True:
	number = int(input("Введите число: "))
	n1 = number % 10
	temp = number // 10
	n2 = temp % 10
	n3 = temp // 10
	summ = n1 + n2 + n3
	mult = n1 * n2 * n3
	print("Сумма цифр: ", summ)
	print("Произведение цифр: ", mult)
	print("")

