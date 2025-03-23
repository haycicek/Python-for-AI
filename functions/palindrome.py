def is_palindrome(word):
    # Reverse control
    if word == word[::-1]:
        return True
    return False

user_word = input("Enter a word to check if it's a palindrome: ").lower()

if is_palindrome(user_word):
    print(f"{user_word} is a palindrome.")
else:
    print(f"{user_word} is not a palindrome.")