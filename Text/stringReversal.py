#String reversal

def reverseString(string):
	ans = ""
	for i in range(len(string)):
		ans += string[-i + -1]
	return ans

reverseString("temp")
