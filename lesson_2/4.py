str = input("Введите строку ")
list = str.split()
i = 1
for elem in list:
	k = len(elem)
	if (k > 10):
		print(i, elem[0:10])
	else:
		print(i, elem)
	i = i + 1