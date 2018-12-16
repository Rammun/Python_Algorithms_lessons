# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

while True:
	year = int(input("Введите год: "))
	if(year % 4 == 0 and year % 100 > 0) or (year % 400 == 0):
		result = "высокосный"
	else:
		result = "не высокосный"

	print(f"Год {year} {result}")
	print("")
