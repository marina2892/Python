def my_func(a, b, c):
	list = [a, b, c]
	list.sort()
	return list[-1] + list[-2]
	
print(my_func(10,5,20))