def grosspayhourscount():
    hours = float(input('Enter Hours:'))
    rate = float(input('Rate:'))
    if hours > 40:
        pay = (40 * rate) + (hours-40) * (1.5* rate)
        return pay
    else:
        pay = hours * rate
        return pay
    print("Pay:", pay)

print(grosspayhourscount())


