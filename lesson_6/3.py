class Worker:
	def __init__(self, name, surname, position, wage, bonus):
		self.dictIncome = {"wage":wage,"bonus":bonus}
		self.name = name
		self.surname = surname
		self.position = position
		self._income = self.dictIncome["wage"] + self.dictIncome["bonus"]
		
class Position(Worker):
	def __init__(self, name, surname, position, wage, bonus):
		super().__init__(name, surname, position, wage, bonus)
	
	def get_full_name(self):
		print(f"{self.surname} {self.name}")
		
	def get_total_income(self):
		print(self._income)
		
		
position1 = Position("Василий", "Васильев", "бухгалтер", 20000, 5000)
print(f"{position1.name} {position1.surname} {position1.position} {position1._income}")
position1.get_full_name()
position1.get_total_income()