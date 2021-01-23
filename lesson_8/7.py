class Complex:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		
	def __add__(self, other):
		return Complex(self.a + other.a, self.b + other.b)
		
	def __mul__(self, other):
		return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
		
	def __str__(self):
		return f"{self.a} + {self.b}i"
		
complex1 = Complex(1, 2)
complex2 = Complex(3, 4)
print(complex1)
print(complex2)
print(complex1 + complex2)
print(complex1 * complex2)
