
def my_func1(x, y):
	return x**y
	
def my_func2(x, y):
	p = abs(y)
	i = 1
	res = 1 / x
	while i < p:
		res = res * (1/x)
		i = i + 1
	return res
	
print(my_func1(5.5,-1))
print(my_func2(5.5,-1))

