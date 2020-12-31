# 4 задание

a = input('Введите целое положительное число ')

b = int(a)
max = b % 10

while b // 10 > 0:
    c = b // 10
    if (c < 10):
        if (c > max): 
            max = c
    else:
        d = c % 10
        if (d > max):
            max = d
    b = c

print(max)