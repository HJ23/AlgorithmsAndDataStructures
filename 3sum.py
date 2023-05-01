
def generate_token(a,b,c):
	tmp =sorted([a,b,c])
	return "".join(map(lambda x:str(x),tmp))

def threesum(nums):
	lookup = {}
	result = []
	pos = set()
	for i,num in enumerate(nums):
		if(not (num in lookup) ):
			lookup[num]=[]
		if(len(lookup[num])<3):
			lookup[num].append(i)
		for i1 in range(len(nums)-1):
			for i2 in range(i1+1,len(nums)) :
				if(-(nums[i1]+nums[i2]) in lookup):
					tmp = lookup[-(nums[i1]+nums[i2])]
					if(len(tmp)>2):
						t = generate_token(nums[i1],nums[i2],-(nums[i1]+nums[i2]))
						if(not (t in pos)):
							pos.add(t)
							result.append([-(nums[i1]+nums[i2]),nums[i1],nums[i2]])
					elif(len(tmp)==2 and ((tmp[0]!=i1 and tmp[0]!=i2) or (tmp[1]!=i1 and tmp[1]!=i2))):
						t = generate_token(nums[i1],nums[i2],-(nums[i1]+nums[i2]))
						if(not t in pos):
							pos.add(t)
							result.append([-(nums[i1]+nums[i2]),nums[i1],nums[i2]])
					elif(tmp[0]!=i1 and tmp[0]!=i2):
						t = generate_token(nums[i1],nums[i2],-(nums[i1]+nums[i2]))
						if(not t in pos):
							pos.add(t)
							result.append([-(nums[i1]+nums[i2]),nums[i1],nums[i2]])
	return result



print(threesum([-1,0,1,2,-1,-4]))
print(threesum([3,0,-2,-1,1,2]))
