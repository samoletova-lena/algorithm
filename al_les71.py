import random


array = [i for i in range(-10,9)]
#print(array)
random.shuffle(array)
print(array)


def bubble_sort(array):
	n = 1
	while n < len(array):
		for i in range(len(array) - 1):
			if array[i] < array[i + 1]:
				array[i], array[i + 1] = array[i + 1], array[i]
		n += 1
		print(array)
	return array

print(bubble_sort(array))
