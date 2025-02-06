# Gerið forrit sem biður notanda um að slá inn streng og eina heiltölu. Forritið á að taka
# síðustu 3 stafi strengsins og gera nýjan streng sem samanstendur af x mörgum eintökum af
# þessum síðustu 3 stöfum gamla strengsins þar sem x er talan sem var slegin inn, síðan skal
# forritið svo prenta nýja strenginn út. 

user_text = input("Enter text: ")
user_number = int(input("Enter a number: "))

letters = user_text[-3:] * user_number
print(letters)
