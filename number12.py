pygequal = "ay"
original = (input("Enter a word:"))
if len(original) > 0 and original.isalpha():
    print(original)
else:
    print("empty")
word = original.lower()
first = word[0]
new_word = word[1:] + first + pygequal
print(new_word)


