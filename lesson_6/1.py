from time import sleep
from itertools import cycle

class TrafficLight:
	dictColor = {'red':7, 'yellow':2, 'green':5}
	
	def running(self, color):
		self.__color = color
		print(self.__color)
		sleep(TrafficLight.dictColor[self.__color])
	
	
light1 = TrafficLight()

for i in cycle(['red','yellow','green']):
	light1.running(i)
	
		
