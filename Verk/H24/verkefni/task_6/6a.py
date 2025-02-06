what_time = int(input("What time is it? : "))

if what_time <= 18:
    print("godan daginn")
elif what_time > 18 and what_time <= 24:
    print("gott kvold")
else:
    print("wrong input")