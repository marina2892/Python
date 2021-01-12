from random import randint
f_o = open("file.txt","w")
with f_o:
	list = [f"{randint(1,300)} " for _ in range(10)]
	f_o.writelines(list)

f_o = open("file.txt","r")	
with f_o:
	str = f_o.readline()
	list = str.split()
	sum = 0
	for el in list:
		sum = sum + int(el)
	print(sum)