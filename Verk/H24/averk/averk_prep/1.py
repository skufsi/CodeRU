# Gerið forrit sem spyr notanda um ártal. Ef árið sem slegið var inn var aldamótaár 
# (eins og 1700, 1800 eða 1900, sem sagt ár sem 100 gengur upp í) þá skal forritið tilkynna
# notanda það með því að segja: „þarna byrjaði ný öld!“, en ef árið markaði árþúsundamót
# (ef 1000 gengur upp í árið, dæmi um þetta eru ár eins og 2000 eða 3000) þá skal það í staðinn
# segja „þarna byrjaði nýtt árþúsund!“. Þar að auki, ef árið var 1964 þá skal forritið 
# segja: „þarna byrjaði saga HR!“ (þess má til gamans geta að HR varð til úr sameiningu upprunalega
# HR sem stofnaður var 1998 og tækniháskóla íslands en hann varð til 1964). Ef ekkert af þessu
# á við þá skal forritið segja: „ósköp venjulegt ár þarna á ferð!“ .

user = int(input("Enter specific year: "))

if user % 1000 == 0:
    print(f"{user} was the start of a new millenia!")
elif user % 100 == 0:
    print(f"{user} was the start of a century!")
elif user == 1964:
    print(f"{user} was the start of the University of Reykjavik's history!")
else:
    print(f"Nothing interesting about {user}")
