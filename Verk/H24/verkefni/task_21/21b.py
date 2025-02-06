# Gerið forrit sem byrjar á að opna skrána Borges.txt (textinn er tilvitnun í argentínska
# rithöfundinn og skáldið Jose Luis Borges) og telur síðan hversu mörg tilvik eru af hverju orði.
# Notið orðabók þannig að orð í textanum verða lyklar í orðabókinni og gildi hvers lykils verður
# hversu oft orðið kemur fyrir í textanum. Látið forritið ykkar að lokum finna hversu mörg orð
# eru í skránni, hvaða orð í textanum er algengast og hversu oft það kemur fyrir og skal
# forritið tilkynna notandanum þessar upplýsingar


dictionary = {}
word_count = 0


with open("Borges.txt", "r") as my_file:
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
print("Number of words in the file: ",sum(dictionary.values()))

pop_word = ""
pop_word_count = 0

for key,value in dictionary.items():
    if value > pop_word_count:
        pop_word = key
        pop_word_count = value
print(f"Most instances were of the word: {pop_word}, it came up {pop_word_count} times")

