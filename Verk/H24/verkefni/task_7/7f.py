# G)	Talnabil – Hropmerkt

# Búið til forrit sem prentar allar tölur á ákveðnu bili og hvað talan er hrópmerkt 
# (þ.e. talan er margfölduð með öllum heiltölum sem eru lægri en viðkomandi tala). 
# Notandinn á að ákveða hvaða bil er valið.
import math

print("\nVið ætlum að prenta allar tölur á línubili sem þú ákveður\nsvo skal læt ég þig fá summuna hrópmerkt\n")

bil_1 = int(input("fyrsta tala i lunubili: "))
bil_2 = int(input("seinni tala i lunubili: "))

summa_linubils = 0

for num in range(bil_1, bil_2):
    summa_linubils += 1

summa_hropmerkt = math.factorial(summa_linubils)
print(f"\nSumman er: {summa_linubils}")
print(f"\nSumman hropmerkt er: {summa_hropmerkt}")