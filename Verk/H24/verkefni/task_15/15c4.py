# Skrifið forrit sem tekur eina jákvæða heiltölu sem inntak, köllum hana size. Inntakið táknar stærð á
# lista. Næst áttu að fylla listann af size mörgum tölum. Þegar því er lokið skaltu prenta út hæsta
# gildið í listanum.

size = int(input("Set size of list (positive & whole number): "))

number_list = []

for i in range(size):
    add_number = int(input("Add number: "))
    number_list.append(add_number)

max_number = max(number_list)

print(f"Your number list: {number_list}")
print(f"The highest number was: {max_number}")