class Matrix:
	def __init__(self, matrix):
		self.matrix = matrix
		self.i = len(self.matrix)
		if (type(self.matrix[0]) == list):
			self.j = len(self.matrix[0])
		else:
			self.j = 0
	
	def __str__(self):
		list1 = ['']
		if self.j != 0:
			for m in range(0, self.i):
				for n in range(0, self.j):
					list1.append(str(self.matrix[m][n]))
				list1.append("\n")
			return ' '.join(list1)
		else:
			for m in range(0, self.i):
				list1.append(str(self.matrix[m]))
			return ' '.join(list1)
			
	def __add__(self, other):
		if (self.i == other.i) and (self.j == other.j):
			mass0 = []
			mass1 = []
			if self.j != 0:
				for m in range(0, self.i):
					for n in range(0, self.j):
						mass1.append(self.matrix[m][n] + other.matrix[m][n])
					mass0.append(mass1)
					mass1 = []
				return Matrix(mass0)
			else:
				for m in range(0, self.i):
					mass0.append(self.matrix[m] + other.matrix[m])
				return Matrix(mass0)
		else:
			print ("матрицы разной размерности")
				
		
		
list1 = [[31, 22], [37, 43], [51, 86]]
list2 = [5,7,6,3,4]
list3 = [[30, 67], [102, 4], [300, 6]]
list4 = [15,17,16,13,44]

matrix1 = Matrix(list1)
print(matrix1)

matrix2 = Matrix(list2)
print(matrix2)

matrix3 = Matrix(list3)
matrix4 = Matrix(list4)

print(matrix1 + matrix3)
print(matrix2 + matrix4)
print(matrix1 + matrix4)
