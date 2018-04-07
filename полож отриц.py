n = int(input("n = "))
if n == 0:
	print("Ноль - однозначное число")
else:
	if n > 0:
		print("Положительное")
	else:
		print("Отрицательное")
	if abs(n) < 10:
		print("однозначное число")
	elif 10 <= abs(n) < 100:
		print("двузначное число")
	else:
		print("трехзначное или более число")
