# Forsetar 1
# Gerið forrit með lista þar sem stök listans eru forsetar bandaríkjanna síðan 1980 (þegar
# Reagan varð forseti). Látið síðan forritið spyrja notanda hvort hann vilji vita
# hverjir hafa verið forsetar fyrir árið 2000 eða síðan árið 2000.
# Síðan gengur forritið yfir listann og prentar út þær upplýsingar sem notandinn bað um.


prez_before2k = ["Ronald Reagan", "George H. W. Bush", "Bill Clinton"]
prez_after2k = ["George W Bush", "Barack Obama", "Donald Trump", "Joe Biden"]
all_prez = prez_before2k + prez_after2k

user = input("viltu vita nofn forseta bandarikjana fyrir eda eftir arid 2000? (F/E): ").upper()

if user == "F":
    print(prez_before2k)
elif user == "E":
    print(prez_after2k)
else:
    print("inslattarvilla")

