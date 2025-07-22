def is_palindrome(s):
    return s == s[::-1]
string = input("Enter a string: ").lower()
print("Is palindrome:", is_palindrome(string))
