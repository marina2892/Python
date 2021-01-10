list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(list)
list_new = [list[i+1] for i in range(len(list)) if (i < (len(list) - 1)) and (list[i] < list[i+1])]
print(list_new)