dict = {"One":"Один","Two":"Два","Three":"Три","Four":"Четыре"}
f_o = open("file.txt","r",encoding = "utf-8")
f_o_new = open("file_new.txt","w")
with f_o:
	for str in f_o:
		list = str.split()
		list[0] = dict[list[0]]
		str_new = " ".join(list)
		f_o_new.write(f"{str_new}\n")

f_o_new.close()