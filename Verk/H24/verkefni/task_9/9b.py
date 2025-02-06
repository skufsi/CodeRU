# Við höfum 2 apa sem ýmist brosa eða brosa ekki. Þeir gætu t.d. 
# heitið a_bros og b_bros en gildi breytanna segja til um hvort þeir brosa eða ekki.
# Ef báðir aparnir brosa eða hvorugur þá er eitthvað að!
# Gerið forrit sem spyr notanda um báða apana og segir svo notanda hvort allt sé í lagi eða ekki.


notanti_a = input("er fyrsti apinn brosandi? (J/N)").lower()
notanti_b = input("er seinnni apinn brosandi? (J/N)").lower()

if notanti_a == notanti_b:
    print("eitthvad er ad!")
else:
    print("okei flott")

    
