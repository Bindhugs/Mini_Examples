# Word Count Program

text = input("Enter a sentence: ")

words = text.split()

word_count = len(words)
char_count = len(text)

print("Number of words:", word_count)
print("Number of characters:", char_count)

freq = {}

for word in words:
    word = word.lower()
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("\nWord Frequency:")
for w, c in freq.items():
    print(w, ":", c)