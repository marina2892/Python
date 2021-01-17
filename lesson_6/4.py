class Car:
	def __init__(self, name, color, is_police, speed):
		self.name = name
		self.color = color
		self.is_police = is_police
		self.speed = speed
		
	def go(self):
		print("Машина поехала")
		
	def stop(self):
		print("Машина остановилась")
		
	def turn(self, direction):
		print(f"Машина повернула {direction}")
		
	def show_speed(self):
		print(self.speed)
		

		
class TownCar(Car):
	def __init__(self, name, color, is_police, speed):
		super().__init__(name, color, is_police, speed)
		
	def show_speed(self):
		if self.speed > 60:
			print("Ваш автомобиль превысил скорость")
		else:
			super().show_speed()

class SportCar(Car):
	def __init__(self, name, color, is_police, speed):
		super().__init__(name, color, is_police, speed)

class WorkCar(Car):
	def __init__(self, name, color, is_police, speed):
		super().__init__(name, color, is_police, speed)
		
	def show_speed(self):
		if self.speed > 40:
			print("Ваш автомобиль превысил скорость")
		else:
			super().show_speed()
		
		

class PoliceCar(Car):
	def __init__(self, name, color, is_police, speed):
		super().__init__(name, color, is_police, speed)
		
		

towncar1 = TownCar('BMW','silver',0,60)
sportcar1 = SportCar('Audi','black',0,200)
workcar1 = WorkCar('Toyota Hiace','silver',0,40)
policecar1 = PoliceCar('Skoda','yellow',1,55)

print(f"Имя towncar: {towncar1.name}, скорость sportcar {sportcar1.speed}, цвет workcar: {workcar1.color}, скорость policecar: {policecar1.speed}")
sportcar1.go()
sportcar1.turn("направо")
sportcar1.stop()

towncar1.speed = 80
towncar1.show_speed()
