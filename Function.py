def factorial(a):
    re = 1
    for i in range(2, a + 1):
        re *= i
    return re

number = int(input("number="))
print(f"{number}! = {factorial(number)}")