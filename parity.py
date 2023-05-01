from utils.utils import *

@benchmark(100000)
def predict1(number):
	parity = 0
	while number:
		parity ^= number&1
		number=number>>1
	return parity

@benchmark(100000)
def predict2(number):
	number^=number>>32
	number^=number>>16
	number^=number>>8
	number^=number>>4
	number^=number>>2
	number^=number>>1
	return number&0x1
predict1(12363)
predict2(12363)

