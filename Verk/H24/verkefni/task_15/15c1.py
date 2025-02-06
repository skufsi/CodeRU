size = int(input("hvad er listinn stor? "))

#listi byrjar tomur
whole_numbers = []

# gerum lykkju eins oft og staerdin a size
for i in range(size):
    next_num = int(input("sladu innn naestu heiltolu (adeins heiltolur). "))
    whole_numbers.append(next_num)


#print heiltolur
for i in whole_numbers:
    print(i, end=", ")