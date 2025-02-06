# Forsetar 4
# Gerið forrit með sama lista og í Forsetar 1. Látið síðan forritið spyrja notanda hver hafi verið
# forseti á undan Ronald Reagan og bætið svari notanda við listann fyrir framan Reagan (en
# það var í raun Jimmy Carter sem var forseti í eitt kjörtímabil á árunum 1977-1981). Gefum
# okkur nú að kosningar 2024 séu liðnar og notandi muni vita hver er orðinn forseti þá. Eftir að
# búið var að bæta við Jimmy Carter þá ætti forritið næst að spyrja hver sé næsti forseti og ef
# það er ekki Joe Biden aftur þá ætti forritið að bæta nýja manninum/konunni við listann. Að
# lokum ætti forritið að prenta út listann eins og hann er eftir þessar breytingar.


prez_list = ["Ronald Reagan", "George H. W. Bush", "Bill Clinton", "George W Bush",
"Barack Obama", "Donald Trump", "Joe Biden"]

add_before = input("hver var forseti a undan Ronald Reagan? : ")
prez_list.insert(0, add_before)
add_after = input("hver var kosinn eftir Joe Biden? : ")
prez_list.append(add_after)

print(f"okei tha er thetta listinn okkar: {prez_list}")


