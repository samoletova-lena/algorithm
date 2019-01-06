# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

size = 10
array = [random.randint (2,size) for _ in range (size)]
print (array)
maxnum = 0
posmax = 0
minnum = 2
posmin = 0
for position,a in enumerate(array):
		if a > maxnum:
			maxnum = a
			posmax = position
for positionm,b in enumerate(array):
		if b <= minnum:
			minnum = b
			posmin = positionm
# print(maxnum)
# print(posmax)
# print(minnum)
# print(posmin)
array[posmax] = minnum
array[posmin] = maxnum
print(array)


