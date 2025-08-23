# Function to check Palindrome (ignoring spaces and case)
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("Nurses Run"))   # True
print(is_palindrome("Hello"))        # False
