def findFactorial(num):
    finalnum = 1;
    for i in range(num):
        finalnum *= i + 1;
    return finalnum

print(findFactorial(5))