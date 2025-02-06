# Gerið forrit sem les inn textaskrána „HanSolo.txt“ sem fylgir prófinu inni á canvas.
# Forritið á að tilkynna notandanum hversu mörg orð koma oftar fyrir en einu sinni í skránni og
# einnig hver var heildarfjöldi orða í skránni. Athugið að tákn eins og kommur eða punktar mega
# ekki teljast hluti af orðum.

# Vísbending: hér gæti verið gott að nota orðabók/uppflettitöflu (en ef nemandi getur leyst þetta verkefni án hennar þá er það samt sem áður leyfilegt). Einnig gætu m.a. föll eins og strengjaaðferðirnar replace og split þurft að koma hér við sögu, auk einhverra orðabókar/uppflettitöfluaðferða eins og t.d. values (samt ekki endilega allra þeirra) en þetta er ekki tæmandi listi yfir þau föll sem gætu nýst ykkur hér.

# Dæmi um úttak:
# „Orð sem koma oftar fyrir en einu sinni eru: 2“
# „Heildarfjöldi orða í skránni er: 37“

han_solo_file = {}

with open("HanSolo.txt", "r") as my_file:
    for line in my_file:
        adjust_text = line.replace(".", " ").replace(",", " ").replace(";", " ")
        word_list = adjust_text.split()
        for word in word_list:
            if word in han_solo_file:
                han_solo_file[word] += 1
            else:
                han_solo_file[word] = 1
        

pop_word = ""
pop_word_count = 0

print("Number of different words: ", len(han_solo_file.items()))

for key,value in han_solo_file.items():
    if value > pop_word_count:
        pop_word = key
        pop_word_count = value
print(f"Most instances were of the word: {pop_word}, it came up: {pop_word_count} times")