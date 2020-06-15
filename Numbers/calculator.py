# A basic claulator function

def main():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    op = str(input("Enter an operator (+-*/): "))

    while op not in ('-','+','*','/'):
        op = str(input("Enter a valid operator (+-*/): "))
    print(number1, op, number2, '=', calculate(number1, number2, op))

def calculate(n,m,op):
    tmp = 0
    if op == '+':
        return n + m
    elif op == '-':
        return n - m
    elif op == '*':
        return n * m
    return n / m

if __name__ == "__main__":
    main()
