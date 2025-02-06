# Gerið forrit sem byrjar á að opna bæði Tesla.txt og Borges.txt. Forritið á að eiga 3 mengi, eitt
# fyrir hvora skrá, eitt sem skal að lokum verða sniðmengi hinna og skal forritið fylla fyrstu 2
# mengin af þeim orðum sem eru í samsvarandi skrá (þar sem mengi getur aðeins haft eitt
# eintak af hverju orði þurfið þið náttúrulega ekki að passa að tvítelja ekki, það breytir því engu
# hér). Snyrtið auk þess orðin í leiðinni (losið þau við t.d. kommur og punkta) og notið síðan &
# virkjann eða mengjaaðferðina intersection til að fylla sniðmengið af þeim orðum sem eru í
# báðum hinum 2 mengjunum. Tilkynnið notanda í lokin hvaða orð séu í báðum mengjum (sem
# sagt hvaða orð eru í báðum skrám).


set_1 = set()
set_2 = set()

with open("Tesla.txt", "r") as tesla_file:
    for line in tesla_file:
        adjust_line = line.replace(".", "").replace(",", "").replace(";", "")
        word_list_1 = adjust_line.split()
        for word in word_list_1:
            set_1.add(word)

with open("Borges.txt", "r") as borges_file:
    for line in borges_file:
        adjust_line = line.replace(".", "").replace(",", "").replace(";", "")
        word_list_2 = adjust_line.split()
        for word in word_list_2:
            set_2.add(word)

set_intersection = set_1 & set_2
print(f"The set intersection of both files is: {set_intersection}")
print(f"Set 1: {set_1}")
print(f"Set 2: {set_2}")

