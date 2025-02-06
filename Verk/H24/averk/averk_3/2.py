
fjoldi_nemenda = int(input("Hvad eru margir nemendur? "))

einkunnir = []

for i in range(fjoldi_nemenda):
    notandi_einkunnir = float(input("Sladu inn einkunn: "))
    einkunnir.append(notandi_einkunnir)

medal_einkunn = sum(einkunnir) / len(einkunnir)
topp_einkunn =  max(einkunnir)
bottom_einkunn = min(einkunnir)
print(f"Einkunnirnar eru: {einkunnir}")
print(f"Medaleinkunn er: {medal_einkunn}, Hæsta einkunn er: {topp_einkunn}, Lægsta einkunn er: {bottom_einkunn}")




