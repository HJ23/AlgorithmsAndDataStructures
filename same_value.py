arr1 = [1,2,3,4,5]
arr2 = [1,2,3,4,4,4,4]
arr3 = [3,3,3,3,3,3]
arr4 = [1,2,2,3]
arr5 = [1,1,1,5,5,5,5,5]
arr6 = [1,1]

def run(arr):
	maxi = -10000000000000
	L,R = 0,0
	for x in range(1,len(arr)):
		if(arr[x]==arr[L]):
			R += 1
		else:
			L = x
			R = x
		if(R-L+1>maxi):
			maxi = R-L+1
	return maxi

print(run(arr1),arr1)
print(run(arr2),arr2)
print(run(arr3),arr3)
print(run(arr4),arr4)
print(run(arr5),arr5)
print(run(arr6),arr6)
