# (Functions) Write a function that takes a string and returns a dictionary with vowels as keys and their counts as values
def vowel_count(s):
    vowels = "aeiouAEIOU"
    result = {}

    for ch in s:
        if ch in vowels:
            if ch in result:
                result[ch] += 1
            else:
                result[ch] = 1
    return result
