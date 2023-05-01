array = [11,23,2,22,34,46,22]


def evenize(array):
	i,j = 0, len(array)-1
	while i<j:
		if(array[i]%2==0):
			i+=1
		else:
			array[i],array[j]=array[j],array[i]
			j-=1

	print(array)

evenize(array)
