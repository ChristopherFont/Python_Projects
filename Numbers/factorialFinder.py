# Factorial Finder - The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops and recursion.

def factorial(x):
	if x <= 1:
		return 1
	return x + factorial(x - 1)
	
print(factorial(4))
