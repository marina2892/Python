from abc import ABC, abstractmethod

class Clothes(ABC):
	@abstractmethod
	def ExpenseCloth(self):
		pass
		
class Coat(Clothes):
	def __init__(self, V):
		self.V = V
	def ExpenseCloth(self):
		return (self.V / 6.5 + 0.5)
		
class Suit(Clothes):
	def __init__(self, H):
		self.H = H
	@property	
	def ExpenseCloth(self):
		return (2 * self.H + 0.3)
		
coat1 = Coat(46)

suit1 = Suit(1.8)

print(coat1.ExpenseCloth())
print(suit1.ExpenseCloth)
