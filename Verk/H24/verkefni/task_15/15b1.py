# Mánaðarhitastig 1
# Gerið forrit sem skráir meðalhitastig síðustu 12 mánuði og finnur síðan hæsta og lægsta
# meðalhitann og tilkynnir notanda. Forritið spyr fyrst um 12 tölur sem eru þá meðalhitastig í
# hverjum mánuði síðasta árið (og geymir þær í lista). Síðan finnur forritið hæstu og lægstu
# töluna í listanum (notið max() og min() föllin) og tilkynnir notanda þær.


weather_list = []

for i in range(1,13):
    add_weather = int(input(f"Average degrees for month {i}: "))
    weather_list.append(add_weather)

max_degree = max(weather_list)
min_degree = min(weather_list)

print(f"Average degrees for every month of the year: {weather_list}")
print(f"The hottest month was {max_degree} degrees.")
print(f"The coldest month was {min_degree} degrees.")