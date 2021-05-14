def changeReturnProgram(cost, money):
    money = money - cost

    print(int(money - (money % 1)), end=" ")
    print("Dollars")

    money = round(money % 1, 2)

    while money > 0:
        if money >= 0.25:
            print("A quarter", end=", ")
            money -= 0.25
        elif money >= 0.10:
            print("A dime", end=", ")
            money -= 0.10
        elif money >= 0.05:
            print("A nickle", end=", ")
            money -= 0.05
        else:
            print("A penny", end=", ")
            money -= 0.01
        money = round(money % 1, 2)

changeReturnProgram(float(input("Enter cost: $")), float(input("Enter amount of money given: $")))