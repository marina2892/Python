from functools import reduce
list = [i for i in range(100,1001,2)]
print(reduce(lambda a,b: a * b, list))