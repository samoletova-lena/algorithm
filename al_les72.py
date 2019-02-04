
# 2. Отсортируйте по возрастанию методом слияния одномерный 
# вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


import random


array = [i for i in range(-10,9)]
#print(array)
random.shuffle(array)
print(array)

#мои потуги
def merge(array1,array2):
	for i in array1:
		for j in array2:
			if i < j:



def merge_sort(array):
    if len(array) > 1:
    	mid = len(array)//2
    	l_ar = [:mid]
    	r_ar = [mid:]
    	merge_sort(l_ar)
    	merge_sort(r_ar)
    	merge_ar(l_ar,r_ar)

    else:
    	return array

    print(s_ar, m_ar, l_ar)
    return merge_sort(s_ar) + m_ar + merge_sort(l_ar)

print(merge_sort(array))


    	l_ar = []
    	for item in array:
    		if item < array[pivot]:
            s_ar.append(item)
        elif item > array[pivot]:
            l_ar.append(item)
        elif item == array[pivot]:
            m_ar.append(item)

# скопировано
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)