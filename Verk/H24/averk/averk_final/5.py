# Gerið forrit sem opnar textaskrána JorgeLuisBorgesQuote.txt sem fylgir með prófinu. 
# Forritið ætti svo að finna út bæði hver er heildarfjöldi orða í skránni og einnig hversu 
# mörg ólík orð er að finna í skránni. Athugið að kommur, punktar og önnur slík tákn mega ekki 
# teljast hluti af orðum og orð ætti að teljast það sama þó það komi fyrir með ýmist há eða 
# lágstöfum (þannig að t.d. You og you ættu að teljast sama orðið hvað varðar fjölda ólíkra orða). 
# Vísbending: hér gæti t.d. verið gagnlegt að nýta sér orðabók/uppflettitöflu og 
# strengjaaðferðirnar replace eða split. 


jlb_file = {}
count = 0

with open("JorgeLuisBorgesQuote.txt", "r") as my_file:
    for line in my_file:
        adjust_text = line.replace(".", " ").replace(",", " ").replace(";", " ")
        word_list = adjust_text.split()
        for word in word_list:
            count += 1
            if word in jlb_file:
                jlb_file[word] += 1
            else:
                jlb_file[word] = 1
    
    print(f"Total words: {count}") 
print("Number of different words: ", len(jlb_file.items()))
