roman_num1 = "MDCCC" # 1800
roman_num2 = "MCDIX" # 1409
roman_num3 = "LVIII" # 58

def convert(roman_number:str) -> int:
	result = 0
	cycle=False
	lookup = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
	for i in range(len(roman_number)):
		if(cycle):
			cycle=False
			continue
		if(len(roman_number)-i >= 2 and lookup[roman_number[i]]<lookup[roman_number[i+1]]):
			result+=lookup[roman_number[i+1]]-lookup[roman_number[i]]
			cycle=True
		else:
			result+=lookup[roman_number[i]]
		print(result)
	return result

print(convert(roman_num3))
