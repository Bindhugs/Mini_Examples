#This will count the number of words in a sentence

sentence = input("Enter the sentence in which you want to count the words: ")

words = sentence.split()
count = len(words)

print("Number of words: ",count)