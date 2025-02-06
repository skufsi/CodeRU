# (20%) Skrifið forrit sem les inn þrjár heiltölur. Forritið á svo að finna út og
#prenta summu jákvæðu talnanna (núll telst hér vera jákvæð tala) sem voru
#slegnar inn og summu neikvæðu talnanna sem voru slegnar inn.

num_1 = int(input("Stimpladu inn heiltolu 1: "))
num_2 = int(input("Stimpladu inn heiltolu 2: "))
num_3 = int(input("Stimpladu inn heiltolu 3: "))

positive_sum = 0
negative_sum = 0

summa1 = 0
summa2 = 0

if num_1 >= 0:
    positive_sum = num_1 + summa1
else:
    negative_sum = num_1 + summa2

if num_2 >= 0:
    positive_sum = num_2 + summa1
else:

    negative_sum = num_2 + summa2

if num_3 >= 0:
    positive_sum = num_3 + summa1
else:
    negative_sum = num_3 + summa2

print(f"jakvæð summa: {positive_sum} neikvæð summa: {negative_sum}")
