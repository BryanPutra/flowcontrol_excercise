def generate_n_chars(num,alphabet):
    result = ""
    for i in range(num):
        result += alphabet
    return result

print(generate_n_chars(9,"B"))
