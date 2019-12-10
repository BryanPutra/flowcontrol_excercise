def reverse(str):
    word = ""
    lengthtext = len(str)
    while lengthtext > 0:
        lengthtext -= 1
        word += str[lengthtext]
    return word
inputtext = input("Enter a word:")

print(reverse(inputtext))



