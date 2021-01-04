str = input("Введите через пробел элементы списка: ")
list = str.split()
print(list)
k = len(list)
if (k % 2 == 0):
	j = k
else: 
	j = k - 1
i = 0
while i < j:
	list[i],list[i+1] = list[i+1],list[i]
	i = i + 2
print(list)