# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
import random

size = 10
array = [random.randint (2,9) for _ in range (size)]
print (array)
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
for a in array:
	if a % 2 == 0:
		count2 += 1
	if a % 3 == 0:
		count3 += 1
	if a % 4 == 0:
		count4 += 1
	if a % 5 == 0:
		count5 += 1
	if a % 6 == 0:
		count6 += 1
	if a % 7 == 0:
		count7 += 1
	if a % 8 == 0:
		count8 += 1
	if a % 9 == 0:
		count9 += 1
print (f"Чисел кратных 2 - {count2}, Чисел кратных 3 - {count3}, Чисел кратных 4 - {count4}")
print (f"Чисел кратных 5 - {count5}, Чисел кратных 6 - {count6},Чисел кратных 7 - {count7}, Чисел кратных 8 - {count8}, Чисел кратных 9 - {count9}")

