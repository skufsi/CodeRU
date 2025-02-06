radius = int(input("Settu inn radius: "))

choice = int(input("Settu '1-flatarmal, '2'-ummal eda '3'-rummal: "))

flatarmal = round(radius * radius * 3.14, 2)
ummal = round(2 * radius * 3.14)
rummal = round(4 * 3.14 * radius, 2)

if choice == 1:
    print(f"Flatarmal hrings: {flatarmal}")
elif choice == 2:
    print(f"Ummal hrings: {ummal}")
elif choice == 3:
    print(f"Rummal hrings: {rummal}")