# H)	Margföldunartafla 1

# Búið til forrit sem skrifar úr eina línu í marföldunartöflu.
# Forritið spyr um hvaða línu eigi að skrifa. 
# Ef t.d. er beðið um línu 3 ætti að skrifast: 
# 3 sinnum tafla: 3 6 9 12 15 18 21 24 27 30

print("Magfoldunartafla, veldu tolu og eg gef ther tofluna\n")

tala_notandi = int(input("settu inn tolu: "))

margf_tala = 0


for num in range(1, 10):
    margf_tala += 1
    tafla_reikn = margf_tala * tala_notandi
    print(f"{tala_notandi} * {margf_tala} = {tafla_reikn}")

