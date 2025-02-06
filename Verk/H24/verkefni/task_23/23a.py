# Klasinn hundur.
# Gerið klasa sem heitir hundur. Hundur á meðlimabreyturnar nafn og aldur og meðlimafallið
# (aðferðina) gelt. Þegar nýtt tilvik af hundi er gert þá er smiðnum rétt nafn og aldur. Ef kallað
# er á aðferðina gelt í klasanum þá prentast einfaldlega út „voff“. Gerið einnig aðalforrit sem
# prófar klasann ykkar með því að gera tilvik af honum, prentar tilvikið og kallar að lokum á gelt
# fallið í tilvikinu.


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Nafn: {}, Aldur: {}".format(self.name, self.age)

    def bark(self):
        return "{}: whoof!".format(self.name)

def main():
    snati = Dog("Snati", 8)
    
    print(snati)
    print(snati.bark())

main()