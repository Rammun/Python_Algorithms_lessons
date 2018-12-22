# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа
# должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности
# деления на ноль, если он ввел 0 в качестве делителя.

while True:
	operator= input("Оператор: ")
	if(operator == '0'):
		print("Программа завершена.")
		break

	left_operand = int(input("Левый операнд: "))
	right_operand = int(input("Правый операнд: "))

	if(operator == "+"):
		result = left_operand + right_operand
	elif(operator == "-"):
		result = left_operand - right_operand
	elif(operator == "*"):
		result = left_operand * right_operand
	elif(operator == "/"):
		if(right_operand == 0):
			result = "Ошибка деления на ноль!"
		else:
			result = left_operand / right_operand
	else:
		result = "Неизвестный оператор!"

	print(f"{left_operand} {operator} {right_operand} = {result}")
	print("")

