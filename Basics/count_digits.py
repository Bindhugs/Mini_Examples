# It counts the digit in a given number

n = int(input("Enter the number in which you want to count the digits: "))

count = 0

if n==0:
    count = 1
else:
    while n > 0:
        n //= 10
        count += 1

print("Number of digits: ",count)
