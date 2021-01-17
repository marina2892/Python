class Road:
	def __init__(self, length, width):
		self._length = length
		self._width = width
		
	def asphalt(self, mass, thickness):
		result = self._length * self._width * mass * thickness
		return (f"{result/1000} т")
		
road1 = Road(20000, 10)
print(road1.asphalt(25, 5))