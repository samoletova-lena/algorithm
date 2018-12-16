# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона. 
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random
leftint = int(input ("Введите целое число, которое будет являться началом диапазона"))
rightint = int(input ("Введите целое число, которое будет являться концом диапазона"))
randomint = random.randint(leftint,rightint)
print (randomint)
leftfloat = float(input ("Введите вещественное число, которое будет являться началом диапазона"))
rightfloat = float(input ("Введите вещественное число, которое будет являться концом диапазона"))
randomfloat = random.uniform(leftfloat, rightfloat)
print (randomfloat)
leftsymbol = ord(input("Введите символ, который будет являться началом диапазона"))
rightsymbol = ord(input("Введите символ, который будет являться концом диапазона"))
#chr
print (leftsymbol)
print (rightsymbol)
if leftsymbol <= rightsymbol:
	randomint = random.randint(leftsymbol,rightsymbol)
print (chr(randomint))
