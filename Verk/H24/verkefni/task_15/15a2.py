# Forsetar 2
# Gerið forrit með sama lista og í Forsetar 1. Látið nú forritið spyrja notandann hvort hann hafi
# einhvern bandarískan forseta í huga og svo athugar forritið hvort við eigum hann í listanum
# okkar (prófið t.d. hvort við eigum George Washington, Jimmy Carter eða Barack Obama).
# Síðan tilkynnir forritið notanda hvort við höfum þennan forseta skráðan hjá okkur (sem sagt
# hvort hann finnst í listanum okkar).

prez_list = ["Ronald Reagan", "George H. W. Bush", "Bill Clinton", "George W Bush",
"Barack Obama", "Donald Trump", "Joe Biden"]

user = input("Ertu med forseta i huga, eg skal athuga hvort hann er a listanum: ")

if user in prez_list:
    print("hann er a listanum")
elif user not in prez_list:
    print("hann er ekki a listanum")
else:
    print("inslattarvilla")



