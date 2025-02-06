# Gerið forrit sem les inn textaskrána „Tesla.txt“ sem fylgir verkefninu. Forritið á að m.a. nota
# uppflettitöflu til að finna hversu mörg eintök af hverju orði eru í skránni. Þá er átt við að
# hvert orð ætti að vera lykill í töflunni og gildi lykilsins verður þá fjöldi þeirra skipta sem 
# orðið kemur fyrir í skránni. Notið einnig viðeigandi föll 
# (þið gætuð t.d. notað split() og strip() föllin) til að skipta línum sem þið lesið úr skrá upp 
# í lista eða til að losa hvert orð við tákn eins og kommur, punkta eða nýlínu (\n) 
# áður en orðið er fært sem lykill inn í uppflettitöfluna. Að lokum ætti forritið að prenta út 
# töfluna okkar svo við sjáum hvernig hún lítur út.


dictionary = {}
word_count = 0

with open("Tesla.txt", "r") as my_file:
    for line in my_file:
        adjust_text = line.replace(",", " ").replace(".", " ")
        word_list = adjust_text.split()
        for word in word_list:
            word_count += 1
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
print(dictionary)
print(f"Number of words in the file are: {word_count}")


