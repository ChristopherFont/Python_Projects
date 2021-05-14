# Fast Exponentiation - Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) in O(lg n) time complexity.

def fastExponentiation(a,b):
	if b == 0:
		return 1
	
	ans = a
	
	while b > 1:
		ans += a
		b -= 1
	return ans

print(fastExponentiation(int(input("Enter a: ")), int(input("Enter b: "))))
