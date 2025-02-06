for num in range(4):
    print("H S " * 4)
    print("S H " * 4)



print("\n\n")


for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            print("H", end=" ")
        else:
            print("S", end=" ")
    print()