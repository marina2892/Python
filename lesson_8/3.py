class Chislo(Exception):
	def __init__(self, txt):
		self.txt = txt
		
list1 = []
while 1:
	c = input("Введите число ")
	if (c == "stop"):
		print(list1)
		break
		
	for el in c:
		try:
			if(ord(el) < 48 or ord(el) > 57):
				raise Chislo("не число")
		except Chislo as err:
			print(err.txt)
			fl = 0
			break
		else:
			fl = 1
	if (fl == 1):
		list1.append(c)