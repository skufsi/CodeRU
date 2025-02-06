borges_file = {}
word_count = 0

with open("BorgesTilvitnun.txt", "r") as my_file:
    for line in my_file:
        adjust_text = line.replace(".", " ").replace(",", " ").replace(";", " ")
        word_list = adjust_text.split()
        for word in word_list:
            word_count += 1
            if word in borges_file:
                borges_file[word] += 1
            else:
                borges_file[word] = 1
        
print(borges_file)

pop_word = ""
pop_word_count = 0

print("Number of different words: ", len(borges_file.items()))

for key,value in borges_file.items():
    if value > pop_word_count:
        pop_word = key
        pop_word_count = value
print(f"Most instances were of the word: {pop_word}, it came up: {pop_word_count} times")
