# Finds the sum of digits

num = int(input("Enter the digits to be added: "))

total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits: ",total)
