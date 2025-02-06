# Skrifið fall sem tekur við tveimur færibreytum og skilar summu þeirra. Látið fallið nota
# try/except setningu til að athuga hvort færibreyturnar séu af réttri tegund
# (hér eruð þið að tékka á TypeError villu). 
# Með öðrum orðum þá eruð þið að prófa hvort færibreyturnar eru örugglega báðar tölur eða báðar
# strengir því þá er hægt að leggja þær saman en annars ekki.
# Ef TypeError villa kemur upp þá á forritið einfaldlega að prenta út einhverskonar
# villutilkynningu svo notandi viti hvað hann gerði rangt. Gerið einnig aðalforrit sem prófar
# fallið ykkar og notið harðkóðuð gildi (t.d. 2 breytur sem báðar eru heiltölur og svo aftur með
# 2 breytum þar sem önnur er heiltala en hin er strengur).

def value_check(number1, number2, sum1):
    try:
        num_type1 = int(number1)
        num_type2= int(number2)
        sum_type = int(sum1)
    except ValueError:
        input("Error: wrong type")

user_num1 = input("enter first number: ")
user_num2 = input("enter second number: ")
user_sum = int(user_num1) + int(user_num2)
value_check(user_num1, user_num2, user_sum)

print(f"Your numbers were: {user_num1} & {user_num2}")
print(f"The sum of these numbers is: {user_sum}")

