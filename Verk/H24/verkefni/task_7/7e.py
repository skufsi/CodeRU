#F)	Talnabil - Summa

#Búið til forrit sem leggur sama allar tölur á ákveðnu bili.
#  T.d. ef bilið er frá 5 upp í 11 á niðurstaðan að vera 5+6+7+8+9+10+11 = 56.
#  Notandinn á að ákveða hvaða bil er valið.

print("\nSettu inn tvær tölur og ég gef þér summuna\ná tölunum sem eru í því línubili\n")

bil_1 = int(input("Byrjun á línubili: "))
bil_2 = int(input("Byrjun á línubili: "))

summa = 0

for num in range(bil_1, bil_2):
    summa += 1

print(summa)

