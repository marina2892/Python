file_object = open("file.txt","w")
s = input("Введите строку ")
while s != "":
	file_object.write(f"{s}\n")
	s = input("Введите строку ")
file_object.close()
