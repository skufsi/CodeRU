first = int(input("insert first number for the range: "))

second = int(input("insert second number for the range: "))

if first == second:
    print("same number doofus")
elif first - second <= 2:
    print("not a big enough range")
else:
    for num in range(first, second + 1):
        print(num)