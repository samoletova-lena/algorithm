# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
import cProfile
# size = 10
# array = [random.randint (-100,100) for _ in range (size)]
# print (array)
# 1. мой  вариант
def minmaxchange(array):
	maxnum = 0
	posmax = 0
	minnum = 0
	posmin = 0
	for position, a in enumerate(array):
		if a > maxnum:
			maxnum = a
			posmax = position
	for positionm, b in enumerate(array):
		if b < minnum:
			minnum = b
			posmin = positionm
			# print(maxnum)
			# print(posmax)
			# print(minnum)
			# print(posmin)
	array[posmax] = minnum
	array[posmin] = maxnum
	return array
list = [17,-19,14,86,9,23,1,0,9,-7,-11]
#print(minmaxchange(list))

# 41.minmaxchange([3, 6, 100500, 666, 9,-4,2])" 7 цифр в массиве
# 100 loops, best of 5: 1.75 usec per loop
# 41.minmaxchange([3, 6, 100500, 666, 9,-4,2,22,14,6,7,8,81,-5,-2,90])" 16 цифр в массиве
# 100 loops, best of 5: 2.75 usec per loop 
# 41.minmaxchange([3, 6, 100500, 666, 9,-4,2,22,14,6,7,8,81,-5,-2,90,11,45.-7,-5,-34,33,56,2,5555532,53,-800])" 27 цифр в массиве
# 100 loops, best of 5: 4.04 usec per loop

# 2. вариант из дз приложенного к уроку
def minmaxchange_norm(array):
	idx_min = 0
	idx_max = 0
	for i in range(len(array)):
		if array[i] < array[idx_min]:
			idx_min = i
		elif array[i] > array[idx_max]:
			idx_max = i
	# print(f'Min = {array[idx_min]} в ячейке {idx_min}; Max = {array[idx_max]} в ячейке {idx_max}')
	spam = array[idx_min]
	array[idx_min] = array[idx_max]
	array[idx_max] = spam
	#print(array)
	return array
# print(minmaxchange_norm(list))

# 41.minmaxchange_norm([3, 6, 100500, 666, 9,-4,2])" 7 цифр в массиве
# 100 loops, best of 5: 2.08 usec per loop
# 41.minmaxchange_norm([3, 6, 100500, 666, 9,-4,2,22,14,6,7,8,81,-5,-2,90])" 16 цифр в массиве
# 100 loops, best of 5: 3.93 usec per loop
# 41.minmaxchange_norm([3, 6, 100500, 666, 9,-4,2,22,14,6,7,8,81,-5,-2,90,11,45.-7,-5,-34,33,56,2,5555532,53,-800])"
# 100 loops, best of 5: 5.91 usec per loop

# 3 Вариант с использованием функций min max и index
def minmaxchange_minmax(array):
	idx_min = 0
	minnum = 0
	idx_max = 0
	maxnum = 0
	minnum = min(array)
	idx_min = array.index(minnum)
	# print(minnum,idx_min)
	maxnum = max(array)
	idx_max = array.index(maxnum)
	# print(maxnum,idx_max)
	array[idx_max] = minnum
	array[idx_min] = maxnum
	return array
	
list = [17,-19,14,86,9,23,1,0,9,-7,-11]
print(minmaxchange_minmax(list))

# 41.minmaxchange_minmax([3, 6, 100500, 666, 9,-4,2])" 7 цифр
# [17, 86, 14, -19, 9, 23, 1, 0, 9, -7, -11]
# 100 loops, best of 5: 1.66 usec per loop
# 41.minmaxchange_minmax([3, 6, 100500, 666, 9,-4,2,22,14,6,7,8,81,-5,-2,90])" - 16 цифр
# [17, 86, 14, -19, 9, 23, 1, 0, 9, -7, -11]
# 100 loops, best of 5: 2.04 usec per loop
# [17, 86, 14, -19, 9, 23, 1, 0, 9, -7, -11] - 27 цифр
# 100 loops, best of 5: 3.25 usec per loop

cProfile.run("minmaxchange([3, 6, 100500, 666, 9,-4,2])")
 # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
 #        1    0.000    0.000    0.000    0.000 al_les41.py:8(minmaxchange)
 #        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run("minmaxchange_norm([3, 6, 100500, 666, 9,-4,2])")
 # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
 #        1    0.000    0.000    0.000    0.000 al_les41.py:39(minmaxchange_norm)
 #        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
 #        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
 #        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run("minmaxchange_minmax([3, 6, 100500, 666, 9,-4,2])")
  # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #       1    0.000    0.000    0.000    0.000 <string>:1(<module>)
  #       1    0.000    0.000    0.000    0.000 al_les41.py:63(minmaxchange_minmax)
  #       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
  #       1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
  #       1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
  #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  #       2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

#выводы: самую высокую скорость показывает вариант с использоавнием встроенных функций min и max, но у нее же самое большое
#количество вызовов ncalls, 