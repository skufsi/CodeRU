# Margföldunartafla 2.
# Búið til forrit með eftirfarandi föllum og látið forritið nota/prófa fallið.
# Búið til tvö föll þar sem annað virkar eins og fallið í Margföldunartöflu 1 og hitt kallar á það
# fall 10 sinnum þannig að margföldunartaflan (frá 1 og upp í 10) prentast út.

def tafla(number):
    for num in range(1, 11):
        print(f"{number} x {num} = {number * num}")

def allar_toflur():
    for i in range(1, 11):
        print(f"\nMargföldunartafla fyrir {i}:")
        tafla(i)

allar_toflur()