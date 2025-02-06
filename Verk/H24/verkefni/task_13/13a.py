# Margföldunartafla 1.
# Búið til forrit með eftirfarandi falli og látið forritið nota/prófa fallið.
# Búið til fall sem skrifar út eina línu í marföldunartöflu.
# Fallinu er rétt raunstiki sem táknar þá línu sem á að skrifa.
# Ef t.d. er beðið um línu 3 ætti að skrifast: 3 sinnum tafla: 3 6 9 12 15 18 21 24 27 30

def tafla(number):
    for num in range(1, 11):
        calc = number * num
        print(calc)
    
user = int(input("hvada margfoldunartoflu viltu fa (1-10): "))
tafla(user)