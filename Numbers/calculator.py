# A basic calculator function

def main():
    number1 = 0
    number2 = 0
    op = " "

    while True:
        try:
            number1 = int(input("Enter a number: "))
            break;
        except ValueError:
            print("Error! Invalid input. Try again.")

    while True:
        try:
            number2 = int(input("Enter another number: "))
            break;
        except ValueError:
            print("Error! Invalid input. Try again.")

    while op not in ('-','+','*','/'):
        op = str(input("Enter a valid operator (+-*/): "))
        print("Error! Invalid input. Try again.")

    print(number1, op, number2, '=', calculate(number1, number2, op))

def calculate(n,m,op):
    if op == '+':
        return n + m
    elif op == '-':
        return n - m
    elif op == '*':
        return n * m
    return n / m

if __name__ == "__main__":
    main()
