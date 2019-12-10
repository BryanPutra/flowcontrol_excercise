def character(str):
    vowels = "aiueoyAIUEOY"
    if str in vowels:
        return True
    else:
        return False

print(character("a"))
print(character("A"))
