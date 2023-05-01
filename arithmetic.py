import math

# mod by 2
def mod2(number,power):
	return 0xFFFFFFFFFFFFFFFF>>(64-power)&number

def powerOf2(number):
	return number!=0 and (number&(number-1))==0

def propagateSetRightMost(number):
	return number|((number-1)^number)

def power(x,y):
	result,power = 1 , y
	while(power):
		if(power&1):
			result*=x
		x,power = x*x , power>>1
	return result

def palindrome1(number):
	tmp=0
	old_number = number
	while(number):
		x = number%10
		tmp = 10*tmp + x
		number = number//10
	return old_number == tmp

