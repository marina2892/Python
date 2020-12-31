# 1 задание
a = 20
b = 'string'
c = 0.6
print(a)
print(b)
print(c)
d = input('Введите число от 0 до 10 ')
print(int(d) + a)
print("%s" %(d))

# 2 задание

t = input('Введите время в секундах ')
h = int(t) // 3600
m = (int(t) - h * 3600) // 60
s = int(t) - h * 3600 - m * 60

print(f"{h:02}:{m:02}:{s:02}")

# 3 задание

n = input('Введите число')
m0 = int(n)
m1 = m0 * 10 + m0
m2 = m1 * 10 + m0
sum = m0 + m1 + m2
print(sum)

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
         
# 5 задание

v = input('Введите выручку фирмы ')
i = input('Введите издержки фирмы ')

v = float(v)
i = float(i)

if v > i:
    print ('Фирма работает с прибылью')
    rent = (v - i) / v
    print (f'Рентабельность фирмы составляет: {rent}')
    c = input('Введите численность сотрудников фирмы ')
    c1 = int(c)
    if c1 > 0:
        print (f'Прибыль фирмы в расчете на одного сотрудника составляет: {(v - i) // c1}')
elif v < i:
    print ('Фирма работает в убыток')
else:
    print ('Убыток и прибыль равны')

# 6 задание

a = input('В первый день спортсмен пробежал (км) ')
b = input('Сколько км спортсмен должен пробегать в день? ')
a = float(a)
b = float(b)
day = 1
res = a
while res < b:
	res = res + res / 10
	day = day + 1
print(f"На {day}-й день спортсмен достиг результата - не менее {b} км")

