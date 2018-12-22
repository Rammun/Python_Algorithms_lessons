# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

from random import randint
while True:
	number = randint(0, 100)
	print("Число загадано, я готов играть!")

	attempt = 0
	result = False
	while (attempt < 10):
		attempt += 1
		n = int(input(f"Попытка {attempt}: "))
		if(number > n):
			print("Мало")
		elif(number < n):
			print("Много")
		else:
			print(f"Угадано!")
			result = True
			break

	if(result == False):
		print("Попытки исчерпаны, вы проиграли! Загаданное число {number}")
	print("")