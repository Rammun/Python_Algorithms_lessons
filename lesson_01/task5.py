# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

# только латинский алфавит
while True:
	first_letter = input("Первая буква: ")
	second_letter = input("Вторая буква: ")
	first_place = ord(first_letter.upper()) - 64
	second_place = ord(second_letter.upper()) - 64
	between_count = abs(second_place - first_place) - 1

	print(f"Местоположение певрой: {first_place}")
	print(f"Местоположение второй: {second_place}")
	print(f"Между ними: {between_count}")
	print("")

