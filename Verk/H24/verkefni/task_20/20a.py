# Skrifið forrit sem spyr notanda að nafni og símanúmeri. Síðan færir það nafnið og símanúmerið inn
# í uppflettitöflu sem lykil og gildi og spyr notanda hvort hann vilji halda áfram.
# Þegar notandi gefur til kynna að hann vilji hætta þá endar forritið á að prenta út uppflettitöfluna.

phonebook = {}
continue_phonebook = "y"

while continue_phonebook == "y":
    name = input("insert next name for the phonebook: ")
    number = int(input("Insert next number for the phonebook: "))
    phonebook[name] = number
    continue_phonebook = input("Do you want to continue? (y/n): ")

print(f"This is your phonebook: {phonebook}")

