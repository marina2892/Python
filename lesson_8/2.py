class Zero(Exception):
    def __init__(self, txt):
        self.txt = txt
        
str1 = input("Введите делимое и делитель через пробел ")
list1 = str1.split()
a = float(list1[0])
b = float(list1[1])

try:
    if (b == 0):
        raise Zero("Деление на ноль")
except Zero as err:
    print(err)
else:
	print(a / b)