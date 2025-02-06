# Klasinn nemandi.
# Gerið klasa sem heitir nemandi. Nemandi á eina meðlimabreytu sem heitir einkunn (og byrjar
# með gildið 10) og 2 aðferðir (meðlimaföll sem heita hækka_einkunn og lækka_einkunn
# (hækka_einkunn hækkar einkunnabreytuna um 10 en lækka_einkunn lækkar hana um 10).
# Að auki á hann __str__ aðferð sem skilar streng sem inniheldur einkunn nemandans. Gerið
# aðalforrit sem prófar klasann ykkar, __str__ fallið hans og báðar aðferðirnar.


class Student:
    def __init__(self, grade):
        self.grade = grade

    def plus_10(self):
        return self.grade + 10
    
    def minus_10(self):
        return self.grade - 10
    
    def __str__(self):
        return "Einkunnin er: {}".format(self.grade)
    
def main():
    anton = Student(70)

    print(anton) 
    print(anton.plus_10())

main()