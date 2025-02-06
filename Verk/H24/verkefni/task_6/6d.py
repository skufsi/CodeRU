ar = int(input("settu inn ar og eg skal segja hvort thad er hlaupaar: "))

if ar % 4 == 0:
    print(f"{ar} er hlaupaar")
elif ar % 4 != 0:
    print(f"{ar} er ekki hlaupaar")