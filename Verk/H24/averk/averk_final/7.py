# Gerið klasann Sívalning. Hann á að hafa tvær meðlimabreytur, radíus og hæð.
# Hann á að sjálfsögðu smið sem tekur við 2 færibreytum sem tákna þá radíus og hæð tilviksins
# sem verið er að gera. Hann skal einnig hafa aðferðina rúmmál sem skal reikna út og skila
# rúmmáli sívalningsins (formúlan fyrir rúmmál sívalnings er: hæð*3.14*radíus*radíus). 
# Útfærið einnig __str__ aðferð sem skilar streng sem inniheldur radíus og hæð hringsins. 
# Gerið að lokum aðalforrit sem spyr notanda um radíus og hæð, býr svo til 1 tilvik af klasanum
# með þær tölur sem notandi valdi og notar svo m.a. aðferðina rúmmál til að tilkynna notanda
# rúmmál sívalningsins.
# Að lokum skal aðalforritið prenta út tilvikið(til að prófa __str__ aðferðina).



class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def Volume(self):
        calc = round(self.height * 3.14 * self.radius * self.radius)
        return f"Rummal sivalnings: {calc:.2f}"
    
    def __str__(self):
        return "Radius: {:.2f}\nHæð: {:.2f}".format(self.radius, self.height)
    
def main():
    user_radius = float(input("settu inn radius: "))
    user_height = float(input("settu inn hæð: "))
    calc = Cylinder(user_radius, user_height)
    print(Cylinder.Volume(calc))
    print(Cylinder.__str__(calc))
main()