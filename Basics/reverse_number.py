# Reverse a number

num = int(input("Enter the number which you want to reverse: "))

rev = 0

while num > 0:
    digit = num % 10
    rev = rev*10 + digit
    num = num // 10

print("Reversed number: ",rev)