# В файле данные записаны построчно, фамилия и оклад разделены пробелом
f_o = open("file.txt", "r", encoding = "utf-8")
with f_o:
	cnt = 0
	sum = 0
	for str in f_o:
		cnt = cnt + 1
		list = str.split()
		if float(list[1]) < 20000:
			print(list[0])
		sum = sum + float(list[1])
print(f"Средняя величина дохода сотрудников составляет {sum/cnt}")