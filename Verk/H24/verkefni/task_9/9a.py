user_str = input("enter ")
my_int = int(user_str)
count = 0

while my_int > 0:
    if my_int % 2 == 1:
        my_int = my_int//2
        print(f"odd {my_int}")
    else:
        my_int = my_int - 1
        print(f"even {my_int}")
    count = count + 1 

print(count)
print(my_int)