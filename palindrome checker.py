def is_palindrome(text):
    return text == text[::-1]

word = input("Enter a word: ")
print("Palindrome!" if is_palindrome(word) else "Not a palindrome.")
