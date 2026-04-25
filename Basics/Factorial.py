# Finds factorial of the given number

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)

num = int(input("Enter a number which you want to find the factorial:  "))

print(f'Factorial: ',factorial(num))