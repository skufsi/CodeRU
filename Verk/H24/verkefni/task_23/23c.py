# Klasinn ferhyrningur.
# Gerið klasann Ferhyrning. Ferhyrningur á tvær meðlimabreytur, lengd og breidd. Hann á
# einnig aðferðirnar (meðlimaföllin) flatarmál og ummál en þær skila flatarmáli og ummáli
# ferhyrningsins. Útfærið einnig __str__ aðferð sem skilar streng sem inniheldur lengd og
# breidd ferhyrningsins. Gerið að lokum aðalforrit sem prófar klasann ykkar, __str__ fallið hans
# og báðar aðferðirnar.

class Square:
    def __init__(self, length, width):
        self.length = length
        self.width = width 
    
    def Area(self):
        calc = self.length * self.width
        return f"The area of the square is {calc} m2"

    def Circumference(self):
        calc = self.length * self.length * self.width * self.width
        return f"The circumference is : {calc}"
    
    def __str__(self):
        return "Length: {}, Width: {}".format(self.length, self.width)
    
def main():
    box = Square(20, 40)
    print(box)
    print(Square.Area(box))
    print(Square.Circumference(box))

main()