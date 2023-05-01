array=[34,12,11,-5,46,5,2,1,2,6,7]

pivot = 12


def arrange(array,pivot):
	smaller = 0
	for index in range(len(array)):
		if(array[index]<pivot):
			array[smaller],array[index] = array[index], array[smaller]
			smaller+=1
	larger = len(array)-1
	for index in range(len(array)):
		if(array[index]>pivot):
			array[larger],array[index] = array[index], array[larger]
			larger -= 1
	print(array)

arrange(array,pivot)
