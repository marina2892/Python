def d(x, y):
	try:
		res = x / y
		return res
	except ZeroDivisionError as e:
		return f"error! {e}"


a = float(input("Введите делимое число "))		
b = float(input("Введите делитель числа "))		
res_d = d(a,b)
print(res_d)
