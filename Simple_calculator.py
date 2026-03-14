#SIMPLE CALCULATOR

while True: 
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Operations are '+','-','*','/','%'")

    op = input("Enter the operator: ")
    
    if op == 'Exit' or 'exit' or 'EXIT':
        print("Exiting Calculator..")
        break
    
    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op =="*":
        print(a*b)
    elif op == "/":
        print(a/b)
    elif op == "%":
        print(a%b)
    else:
        print("Invalid operator..")