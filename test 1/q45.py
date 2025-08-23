# Problem Solving) Write a program to count the number of consonants in a string.
s = "hello world"
vowels = "aeiou"
count = 0

for ch in s.lower():
    if ch.isalpha() and ch not in vowels:
        count += 1

print("Consonants:", count)