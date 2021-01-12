dict = {}
f_o = open("file6.txt","r",encoding = "utf-8")
with f_o:
	for str in f_o:
		list = str.split(":")
		list2 = list[1].split()
		sum = 0
		for el in list2:
			index = el.find("(")
			if (index != -1):
				h = int(el[0:index])
				sum = sum + h
		dict.update({list[0]:sum})
	print(dict)