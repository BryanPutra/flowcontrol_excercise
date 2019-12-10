def reverse(str):
    word = ""
    lengthtext = len(str)
    while lengthtext > 0:
        lengthtext -= 1
        word += str[lengthtext]
    return word

def is_palindrome(str):
    if str == reverse(str):
        return True
    else:
        return False

inputtext = input("Enter a word:")
print(is_palindrome(inputtext))
