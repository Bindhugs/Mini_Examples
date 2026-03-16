#Counts the vowels in a string

string = input("Enter a string: ")
count = 0
for vowels in string:
    if vowels in 'aeiouAEIOU':
        count = count+1
print("Number of vowels in the string: ", count)