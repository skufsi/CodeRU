number_str = input("Input a floating-point number: ")

while True:
    try:
        number_float = float(number_str)
        break
    except ValueError:
        number_str = input("try again, put floating value ")
print("Number is",number_float)