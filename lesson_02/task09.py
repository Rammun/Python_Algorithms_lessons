# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

while True:
	number = 0
	max_sum = 0
	while True:
		inpStr = input("Число: ")
		if(inpStr == "-"):
			break
		current_number = int(inpStr)
		number_sum = 0
		temp = current_number
		while temp != 0:
			number_sum += temp % 10
			temp //= 10
		if(max_sum < number_sum):
			max_sum = number_sum
			number = current_number

	print(f"Число: {number}, сумма: {max_sum}")
	print("")

