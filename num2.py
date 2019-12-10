def max_of_three(num1,num2,num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3

print(max_of_three(5,7,2))
print(max_of_three(7,2,4))
print(max_of_three(6,5,7))