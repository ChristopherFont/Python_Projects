#finds the perimeter of an array
def perimeter(sideLengths):
    sum = 0
    for length in sideLengths:
        sum += length
    return sum

print(perimeter([5,5,5,5]))
