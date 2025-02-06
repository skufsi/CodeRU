# Skrifið forrit sem tekur eina jákvæða heiltölu sem inntak, köllum hana size.
# Inntakið táknað stærð á lista. Næst áttu að fylla listann af size mörgum tölum.
# Þegar því er lokið skaltu prenta út meðaltal stakanna í listanum.

size = int(input("Insert a positive whole number for the size of the list: "))

numbers = []

for i in range(size):
    set_number = int(input("Add number: "))
    numbers.append(set_number)

average = sum(numbers) / len(numbers)
print(f"Your number list: {numbers}")
print(f"The average of the list is: {average}")