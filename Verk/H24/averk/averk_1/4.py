print("nu reynir a, hvad er dagsetningin i dag?\n")

manadardagur = int(input("hvaða mánaðadagur er í dag? (svaraðu með tölustöfum) : "))

manudur = input("hvaða manudur er í dag? : ").lower()

artal = int(input("hvaða ár er núna? (svaraðu með tölustöfum) : "))


if manadardagur == 25 and manudur == "október" and artal == 2024:
    print("Rétt")
else:
    print("rangt!")