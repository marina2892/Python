from itertools import count
from itertools import cycle

for x in count(3):
	if x <= 10:
		print(x)
	else:
		break
		
list = ['a','b','c']
i = 0
for x in cycle(list):
	if i < 10:
		print (x)
		i = i + 1
	else:
		break