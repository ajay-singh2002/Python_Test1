# (Functions with Loops) Write a function that counts vowels in a string.def count_vowels(text):
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


print(count_vowels("Ajay Singh"))