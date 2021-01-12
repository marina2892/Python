cnt = 0
dict = {}
with open("file.txt","r") as f_o:
	for str in f_o:
		cnt = cnt + 1
		cnt_words = str.count(" ") + 1
		dict.update({cnt:cnt_words})
print(dict)