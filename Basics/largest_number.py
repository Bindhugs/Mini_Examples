#This will show the largest of 3 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(f'{a} is the largest element among {a},{b},{c}')
elif b > c and b > a:
    print(f'{b} is the largest element among {a},{b},{c}')
else:
    print(f'{c} is the largest element among {a},{b},{c}')
