nums1=[1,2,3,5,5,1] # 3
nums2=[2,-1,1] # 0
nums3=[1,1,1,1,1,1] # -1

def find(nums):
	hash1= {-1:0}
	hash2= {len(nums):0}
	total=0
	for i,x in enumerate(nums):
		total+=x
		hash1[i]=total
	total=0
	for i,x in enumerate(nums[::-1]):
		total+=x
		hash2[len(nums)-i-1]=total
	for key,value in hash1.items():
		if(key+2 in hash2 and hash2[key+2]==value):
			return key+1
	return -1

print(find(nums1))
print(find(nums2))
print(find(nums3))
