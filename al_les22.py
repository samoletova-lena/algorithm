# 2. Посчитать четные и нечетные цифры введенного натурального числа. 
# Например, если введено число 34560, 
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a = int(input("Введите число "))
numchet = 0
numnechet = 0
while a != 0:
        b = a%10
        a = a//10
        if b%2 == 0:
        	numchet += 1
        else:
        	numnechet += 1
print("Кол-во четных цифр числа {}, количество нечетных цифр числа {}".format(numchet, numnechet))
