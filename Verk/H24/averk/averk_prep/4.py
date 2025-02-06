# Gerið forrit sem biður notanda um að slá inn streng. Síðan biður forritið notanda um að velja
# tölu, köllum hana x. Að lokum spyr forritið hvort prenta skuli út strenginn í venjulegri/réttri
# röð, eða öfugri röð. Síðan prentar forritið út x-ta hvern staf í strengnum í þeirri röð sem 
# notandi bað um. T.d. ef notandi sló inn strenginn „Regal“, valdi töluna 1 og bað um öfuga röð
# þá myndi forritið prenta út strenginn „lageR“. En ef notandi hefði t.d. slegið inn „Venison“,
# valið töluna 3 og beðið um rétta röð þá hefði forritið prentað út strenginn „Vin“.


user_text = input("Enter text: ")
user_number = int(input("Enter a number: "))
order = int(input("Enter '1' for normal order and '2' for reverse: "))

if order == 1:
    print(user_text[:: user_number])
elif order == 2:
    print(user_text[:: -user_number])
