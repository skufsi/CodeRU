# I)	Margföldunartafla 2

# Búið til hreiðraða lykkju (þ.e. lykkju innan í lykkju) sem skrifar út 1 - 10 sinnum
#  margföldunartöflurnar. (þ.e. 1 sinnum töfluna, 2 sinnum töfluna o.s.frv. 
# upp í 10 sinnum töfluna)


tala = 0
margf_tala = 0

for tala_1 in range(1,11):
    margf_tala += 1
    print(f"----------\nTafla {margf_tala}\n----------\n", end="")
    for tala_2 in range(1, 11):
        tafla = margf_tala * tala_2 
        print(f"{margf_tala} * {tala_2} = {tafla}")