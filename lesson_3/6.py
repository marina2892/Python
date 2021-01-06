def int_func(str):
	
	return str.capitalize()
	
a = input("Введите слово из маленьких латинских букв ")
result = int_func(a)
print(result)

a = input("Введите строку из слов, разделенных пробелом ")
list = a.split()
list2 = []
for elem in list:
	list2.append(int_func(elem))
print(" ".join(list2))
	

