#PALINDROME CHECKER

word = input("Enter your word: ")

if word == word[: : -1]:
    print("The word is palindrome")

else:
    print("The word is not palindrome")
