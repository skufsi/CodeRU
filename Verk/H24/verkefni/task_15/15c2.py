# Skrifið forrit sem tekur eina jákvæða heiltölu sem inntak,
# köllum hana size. Inntakið táknar stærð á lista.
# Næst áttu að fylla listann af size mörgum tölum.
# Þegar því er lokið skaltu prenta út summu stakanna í listanum.


print("Welcome, insert the size of your list \nafterwards you'll need to input numbers for the list")
print("\nFinally i will give you the list and the sum of the numbers\n")

size = int(input("Size of list: "))

numbers = []
list_sum = 0

for i in range(size):
    set_number = int(input("Add number: "))
    numbers.append(set_number)

for i in (numbers):
    list_sum += i


print(f"\nYour list: {numbers}")
print(f"\nThe sum of your numbers: {list_sum}")