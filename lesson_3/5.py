def func(*args):
	sum = 0
	fl = 0
	for elem in args:
		if ord(elem) < 48 or ord(elem) > 57:
			fl = 1
			break
		else:
			elem = float(elem)
			sum = sum + elem
	return {'sum':sum, 'fl':fl}

result = 0	
while 1:
	a = input("Введите числа через пробел ")
	list = a.split()
	res = func(*list)
	result = result + res['sum']
	print(result)
	fl = res['fl']
	if fl == 1:
		break