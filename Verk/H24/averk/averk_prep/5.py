# Gerið fallið flatarmál_hrings sem tekur við einni færibreytu (radíus hringsins) og skilar
# flatarmáli hrings með þann radíus. Gerið einnig fallið rúmmál_kúlu sem tekur við einni
# færibreytu (radíus kúlunnar) og skilar rúmmáli kúlu með þann radíus. Gerið svo aðalforrit
# sem prófar föllin ykkar með því að spyrja notandann fyrst hver sé radíusinn, síðan hvort hann
# vilji reikna flatarmál eða rúmmál, svo er kallað á viðeigandi fall til að framkvæma útreikningana
# og að lokum tilkynnir aðalforritið notandanum niðurstöðuna. Formúlan fyrir flatarmál hrings er
# radíus*radíus*pí  og Formúlan fyrir rúmmál kúlu er: 
# 〖4*π*r〗^3/3 (í báðum tilfellum er í lagi að nota 3.14 fyrir pí).

radius = int(input("Enter radius of circle: "))
choice = int(input("Enter '1' for area and '2' for volume: "))

area = round(radius * radius * 3.14, 2)
volume = round(4 * 3.14 * radius, 2)

if choice == 1:
    print(f"Area of the circle: {area}")
elif choice == 2:
    print(f"Volume is: {volume}")