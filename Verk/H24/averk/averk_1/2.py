tala_notandi = int(input("settu inn tolu og sjaum hvort hun se slett eda oddatala: "))

if tala_notandi % 2:
    print(f"{tala_notandi} er oddatala")
elif tala_notandi % 2 == False:
    print(f"{tala_notandi} er slett tala")
else:
    print("villa")