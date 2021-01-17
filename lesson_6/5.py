class Stationery:
	def __init__(self, title):
		self.title = title
		
	def drow(self):
		print("Запуск отрисовки.")
		
class Pen(Stationery):
	def __init__(self, title):
		super().__init__(title)
		
	def drow(self):
		print(f"Запуск отрисовки ручкой {self.title}.")

class Pencil(Stationery):
	def __init__(self, title):
		super().__init__(title)
		
	def drow(self):
		print(f"Запуск отрисовки карандашом {self.title}.")

class Handle(Stationery):
	def __init__(self, title):
		super().__init__(title)
		
	def drow(self):
		print(f"Запуск отрисовки маркером {self.title}.")
		
pen1 = Pen('Ручка erich krause')
pencil1 = Pencil('Карандаш HB')
handle1 = Handle('Маркер Fr-1')

pen1.drow()
pencil1.drow()
handle1.drow()
