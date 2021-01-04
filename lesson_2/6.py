n = input("Введите количество товаров для ввода ")
list = []
i = 0
while i < int(n):
	str = input("Введите через ',' параметры товаров: название, цена, количество, единица измерения ")
	l = str.split(",")
	list.append((i+1,{"название":l[0],"цена":l[1],"количество":l[2],"ед":l[3]}))
	i = i + 1

name = []
price = []
count = []
si  = []

i = 0
while i < int(n):
	name.append(list[i][1]["название"])
	price.append(list[i][1]["цена"])
	count.append(list[i][1]["количество"])
	si.append(list[i][1]["ед"])
	i = i + 1
	
dict = {"название":name,"цена":price,"количество":count,"ед":si}
print(dict)

