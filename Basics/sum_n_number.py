# Sum of n numbers

num = int(input("Enter a number: "))

total = 0
for i in range(1, num+1):
    total += i

print("The sum of the first", num, "numbers is:", total)
