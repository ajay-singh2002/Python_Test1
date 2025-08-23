# Print all unique words from a sentence in alphabetical order
sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = sorted(set(words))

print("Unique words in alphabetical order:")
for word in unique_words:
    print(word)