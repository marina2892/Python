list = [10, 8, 8, 6, 3, 3]
a = input("Введите элемент рейтинга ")
a = int(a) 
if a > 0:
	fl = 0
	i = len(list) - 1
	for elem in list[::-1]:
		if a <= elem:
			list.insert(i+1,a)
			fl = 1
			break
		i = i - 1
	if fl == 0:
		list.insert(0,a)
	print(list)
else:
	print("Вы ввели недопустимый элемент рейтинга")