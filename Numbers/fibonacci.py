#prints out the fibonacci sequence to the nth time provided in the argument
def fibonacci(maxCount):
    olda = 0
    a = 0
    b = 1

    for i in range(maxCount):
        olda = a
        a = a + b
        b = olda
        print(olda, end=" ")
    print()
