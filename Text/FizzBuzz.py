# Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.


def fizzbuzz(x):
	for i in range(1, x + 1):
		print("%d: " % i, end="")
		if i % 3 == 0:
			print("Fizz", end="")
		if i % 5 == 0:
			print("Buzz", end="")
		print()
			
fizzbuzz(100)
