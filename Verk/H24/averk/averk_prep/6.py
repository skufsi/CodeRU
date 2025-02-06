# Gerið klasann Kúlu. Kúla á breytuna radíus (radíus er þá meðlimabreyta eða á ensku
# „member variable“ klasans), smið (sem tekur við radíus frá notanda þegar kallað er á smiðinn
# og gerir tilvik með þeim radíus), strengjaútgáfu sem skilar streng með radíus kúlunnar 
# (þannig að hægt sé að prenta tilvik af klasanum) og fallið rúmmál_kúlu sem reiknar rúmmál 
# kúlunnar og skilar því. Formúlan fyrir rúmmál kúlu er:  
# 〖4*π*r〗^3/3  (hér er í lagi að nota 3.14 fyrir pí). Látið svo aðalforritið prófa klasann með
# því að spyrja notanda um radíus, gera tilvik af kúlu með þann radíus og tilkynna notanda 
# rúmmál hennar ( með aðstoð aðferðarinnar rúmmál_kúlu ). 

# Prentið að lokum út tilvikið með print fallinu.
# Dæmi um inntak og úttak:
# Úttak:
# „sláðu inn radíus kúlu. „
# Inntak:
# 10
# Úttak:
# „Rúmmál kúlunnar er: 4186.67„
# „Radíusinn er 10.0“
# (athugið að ekki skiptir máli nákvæmlega hversu marga aukastafi þið birtið í þessum svörum) 



class Ball:
    def __init__(self, radius):
        self.radius = radius
    
    def Volume(self):
        calc = round(4 * 3.14 * self.radius, 3)
        return f"The volume of the circle: {calc:.2f}"
    
    def __str__(self):
        return "The radius of the circle: {:.2f}".format(self.radius)
    
def main():
    number = Ball(393.2)
    print(Ball.Volume(number))
    print(number)

main()