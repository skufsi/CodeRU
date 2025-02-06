# Íkornar í Palo Alto í Kaliforníu eyða stundum deginum sínum í að leika sér.
# Ef hitastigið er milli 60 og 90 gráður fahrenheit (60 og 90 meðtaldar)
# þá fer dagurinn í leiki. Þar að auki þá hækka efri mörkin upp í 100 gráður
# ef það er sumar. Látið forritið spyrja notanda um hitastigið og hvort það er sumar eða ekki.
# Síðan á forritið að tilkynna notanda hvort íkornarnir séu að leik þennan daginn eða ekki.


notandi_hitastig = int(input("hvad er hitastigid? "))
notandi_sumar = input("er sumar? (j/n) ").lower()

if notandi_sumar == "j":
    if notandi_hitastig >= 60 and notandi_hitastig <= 100:
        print("leikur hja ikornum")
    elif notandi_hitastig < 60 or notandi_hitastig > 100:
        print("ekki leikur samt sumar :(")
    else:
        print("inslattarvilla")
elif notandi_sumar == "n":
    if notandi_hitastig >= 60 and notandi_hitastig <= 90:
        print("leikur hja ikornum samt ekki sumar!")
    elif notandi_hitastig < 60 or notandi_hitastig > 90:
        print("ekki leikur hja ikornum")
    else:
        print("inslattarvilla")
else:
    print("inslattarvilla")