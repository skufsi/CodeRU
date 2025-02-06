# Skrifið forrit sem biður notanda um að slá inn heiltölu.
# Látið forritið nota try/except setningu til að athuga hvort
# inntakið (innsláttur notanda) sé ekki örugglega heiltala
# (hér eruð þið að tékka á ValueError villu). Ef allt er í lagi
# á forritið að prenta út „Inntak er í lagi“ en annars
# „Inntak er ekki heiltala“ (hvort sem það er af því inntakið var
#  strengur eða fleytitala).

user_number = input("enter a whole number: ")

while True:
    try:
        number_check = int(user_number)
        print(f"Your number {user_number} is a whole number!")
        break
    except ValueError:
        user_number = input("Please insert a whole number: ")
        
        