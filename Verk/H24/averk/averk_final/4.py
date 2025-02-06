# Hvaða tala er tvíundarkerfistalan (binary number) 111010 í okkar talnakerfi ? Sýnið
# útreikninga eða annan rökstuðning í svari ykkar.


# 111010 er í raun 58.
# Þetta sést á því að tölurnar tákna 1 eða 0 sinnum 2 í einhverju veldi, frá hægri
# byrja veldin á 0 og hækka svo um einn eftir því sem við færumst til vinstri.

print("111010: ", 1*2**5 + 1*2**4 + 1*2**3 + 0*2**2 + 1*2**1 + 0*2**0) # = 58