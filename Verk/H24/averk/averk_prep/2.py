# Gerið forrit sem spyr notanda um talnabil og hvort hann vilji að bilið sé prentað út í vaxandi
# eða minnkandi röð. Síðan prentar forritið út allar tölur á bilinu nema þær sem eru margfeldi
# af 3 eða 5, og í þeirri röð sem notandi bað um.

user1 = int(input("Insert first number: "))
user2 = int(input("Insert second number: "))

num_order = input("Enter: 'i' for increasing order and 'd' for decreasing order: ").lower()

if num_order == "i":
    if user1 <= user2:
        for i in range(user1, user2 + 1):
            if i % 3 == True or i % 5 == True:
                print(i)
    elif user1 >= user2:
        for i in range(user2, user1 + 1):
            if i % 3 == True or i % 5 == True:
                print(i)

if num_order == "d":
    if user1 <= user2:
        for i in range(user2, user1 - 1, -1):
            if i % 3 == True or i % 5 == True:
                print(i)
        
    elif user1 >= user2:
        for i in range(user1, user2 - 1, -1):
            if i % 3 == True or i % 5 == True:
                print(i)