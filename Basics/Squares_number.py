#Squares the number

numbers = [1,2,3,4,5,6]

result1 = [x*x for x in numbers if x%2==0] #for even number
result2 = [x*x for x in numbers if x%2!=0] #for odd number

print("Squares of even numbers: ",result1)
print("Squares of odd number: ",result2)
