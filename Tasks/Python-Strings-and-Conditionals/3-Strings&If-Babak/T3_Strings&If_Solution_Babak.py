text = input()

normalized_text = text.lower()

reversed_text = normalized_text[::-1]

is_palindrome = normalized_text == reversed_text

if is_palindrome:
    print("Yes")
else:
    print("No")
