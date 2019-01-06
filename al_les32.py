# Во втором массиве сохранить индексы четных элементов первого массива
import random

size = 10
array = [random.randint (2,size) for _ in range (size)]
b = 0
array2 = []
print (array)
for index, name in enumerate(array):
	if name % 2 == 0:
		b = index
		array2.append(b)
print(array2)
		

