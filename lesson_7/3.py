class Kletka:
	def __init__(self, cell):
		self.cell = cell
		
	def __str__(self):
		return f"Количество ячеек данной клетки: {self.cell}"
		
	def __add__(self, other):
		return Kletka(self.cell + other.cell)
		
	def __sub__(self, other):
		if (self.cell - other.cell > 0):
			return Kletka(self.cell - other.cell)
		else:
			print ("разность < 0")
			
	def __mul__(self, other):
		return Kletka(self.cell * other.cell)
		
	def __truediv__(self, other):
		cell_res = round(self.cell / other.cell)
		return Kletka(cell_res)
        
	def make_order (self, q):
		list1 = []
		n = self.cell // q
		k = self.cell % q
		for i in range(0, n):
			for j in range(0, q):
				list1.append("*")
			list1.append("\n")
		if k != 0:
			for x in range(0, k):
				list1.append("*")
		return ''.join(list1)
			
kletka1 = Kletka(30)
kletka2 = Kletka(40)
kletka3 = Kletka(50)

kletka4 = kletka1 + kletka2 + kletka3
print(kletka4)

kletka5 = kletka2 - kletka1
try:
	print(kletka5)
except Exception:
	print("Обращение к данному объекту невозможно")
	

kletka6 = kletka1 * kletka2 * kletka3
print(kletka6)

kletka7 = kletka2 / kletka1
print(kletka7)

print(kletka1.make_order(7))

	