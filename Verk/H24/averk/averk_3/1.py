hofudborgir = ["Róm", "Washington", "Reykjavík", "París", "Kaupmannahöfn"]

notandi_borg = input("Sláðu inn nafnið á höfuðborg og ég athuga hvort hún sé á listanum: ")

if notandi_borg in hofudborgir:
    print(f"Yess! {notandi_borg} er á listanum!\nHérna er listinn: {hofudborgir}")
elif notandi_borg not in hofudborgir:
    print("ohh demit þessi borg er ekki á listanum")
    add_borg = input("Viltu bæta borginnni við? (Y/N): ").lower()
    if add_borg == "y":
        hofudborgir.append(notandi_borg)
        print(f"Svona er listinn núna: {hofudborgir}")
    elif add_borg == "n":
        print(f"Allt í góðu, hér er listinn: {hofudborgir}")
    else:
        print("Villa! þarf að skrifa (Y/N)")
else:
    print("Inslattarvilla!")
