# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

while True:
	a = int(input("a="))
	b = int(input("b="))
	c = int(input("c="))

	if(b > a > c) or (b < a < c):
		medium = a
	elif(a < b < c) or (a > b > c):
		medium = b
	else:
		medium = c

	print("Среднее: ", medium)
	print("")