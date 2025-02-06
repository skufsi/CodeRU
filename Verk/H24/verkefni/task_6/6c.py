aldur = int(input("Hvad er aldurinn thinn? : "))

if aldur >= 0 and aldur <= 6:
    prin("nu thu ferd ad byrja i skola")
elif aldur >= 7 and aldur <= 15:
    menntaskoli = input("ja okei ert thu ad fara byrja i menntaskola? (J/N): ").lower()
    if menntaskoli == "j":
        print("vo kul")
    elif menntaskoli == "n":
        print("ah dem")
    else:
        print("inslattarvilla")
elif aldur >= 16 and aldur <= 106:
    print("ohh dem thetta forrit er ekki fyrir thig")
else:
    print("inslattarvilla")