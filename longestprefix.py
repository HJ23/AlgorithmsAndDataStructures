strs1 = ["flower","flo","fle","fl23232"]
strs2 = ["dog","doggo","car"]
strs3 = ["flower","flight","flow","f"]

def longestCommonPrefix(strs) -> str:
	minimum_word = strs[0]
	for word in strs:
		if(len(word)<len(minimum_word)):
			minimum_word = word
	for word in strs:
		if( word[:len(minimum_word)] == minimum_word ):
			continue
		for index in range(0,len(minimum_word)):
			minimum_word = minimum_word[:len(minimum_word)-1]
			print(minimum_word)
			if(word[:len(minimum_word)] == minimum_word):
				break
	return  minimum_word

def longestCommonPrefix2(strs) -> str:
	result=""
	reference = strs[0]
	for index in range(len(reference)):
		counter=0
		for word in strs:
			if(index==len(word) or word[index]!=reference[index]):
				return result
			if(word[index]==reference[index]):
				counter+=1
		if(counter==len(strs)):
			result+=reference[index]
		else:
			break
	return result

print(longestCommonPrefix2(strs1))
print(longestCommonPrefix2(strs2))
print(longestCommonPrefix2(strs3))
