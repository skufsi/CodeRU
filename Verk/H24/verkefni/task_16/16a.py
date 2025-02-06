# Gerið forrit sem les inn textaskrána SV1.txt sem fylgir verkefninu og gerið forrit sem opnar
# skrána og gerir nýja skrá (sem gæti t.d. heitið SV1_lagað.txt) sem hefur sama innihald nema
# nú er búið að fjarlægja öll bil milli orða og einnig öll línubil („\n“). Þannig að í nýju skránni
# kemur allur textinn í einni línu án bils milli orða.Hér gæti t.d. verið hentugt að nýta sér
# replace() strengjaaðferðina.


with open("SV1.txt", "r") as skra_inn, open("SV1_a_lagað.txt", "w") as skra_ut:
    for line in skra_inn:
        snyrt_lina = line.replace(" ", "").replace("\n", "")
        skra_ut.write(snyrt_lina)