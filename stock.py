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

# O(n)
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
