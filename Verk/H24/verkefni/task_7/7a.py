tala_notandi = int(input("settu inn tolu: "))
print(f"talan thin er: {tala_notandi}")
svar = input("viltu halda afram? (J/N)").lower()

tolur = []
tolur.append(tala_notandi)

while svar == "j":
    tala_notandi = int(input("settu inn tolu: "))
    tolur.append(tala_notandi)
    print(f"tolurnar thinar eru : {tolur}")
    svar = input("viltu halda afram? (J/N)").lower()
print("takk fyrir ad spila")