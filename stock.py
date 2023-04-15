from utils.utils import *

STOCK = [10,20,14,12,19,24,7,9,12,14,15,19,34,56,34,23]


# 0(n^2)
@benchmark(1000000)
def predict1(array):
	MAX = 0
	for i,x in enumerate(array[:-1]):
		for y in array[i+1:]:
			if((y-x)>MAX):
				MAX= y-x
	return MAX

# O(nlog(n))
@benchmark(1000000)
def predict2(array):
	SORTED_ARRAY = []
	for i,x in enumerate(array):
		SORTED_ARRAY.append((i,x))
	SORTED_ARRAY = sorted(SORTED_ARRAY , key = lambda x:x[1])
	MAX = 0
	half = len(SORTED_ARRAY)//2
	full = len(SORTED_ARRAY)-1
	for i in range(half+1):
		if( ( (SORTED_ARRAY[full-i][1]-SORTED_ARRAY[i][1]) > MAX ) and (SORTED_ARRAY[full-i][0]>SORTED_ARRAY[i][0])):
			MAX = SORTED_ARRAY[full-i][1]-SORTED_ARRAY[i][1]
	return MAX

@benchmark(1000000)
def predict3(array):
	MIN_ELEMENT = 1000000000
	MAX = 0
	for x in array:
		if(x<MIN_ELEMENT):
			MIN_ELEMENT = x
		else:
			if( (x-MIN_ELEMENT) > MAX):
				MAX = x-MIN_ELEMENT
	return MAX

predict1(STOCK)
predict2(STOCK)
predict3(STOCK)
