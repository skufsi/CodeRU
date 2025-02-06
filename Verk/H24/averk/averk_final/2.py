# Gerið forrit sem spyr notanda um talnabil. Síðan prentar forritið út allar tölur á bilinu
# nema þær sem eru margfeldi af 3 eða 8.


user1 = int(input("Insert first number: "))
user2 = int(input("Insert second number: "))

for i in range(user1, user2 + 1):
    if i % 3 == True or i % 8 == True:
        print(i)
