
#Uprav program tak, aby proměnou zacatek_lekce převedl na datetime

# from datetime import datetime
# zacatek_lekce = "7. 11. 2024 18:00"
# # Doplň kód do uvozovek
# zacatek_lekce = datetime.strptime(zacatek_lekce, "%d. %m. %Y %H:%M")
# nazev_dne = zacatek_lekce.strftime("%A")



# print(zacatek_lekce)                #"%d. %m. %Y, %H:%M"
# print(zacatek_lekce.isoformat())
# print(nazev_dne)

# from datetime import datetime
# zacatek_lekce = "7. 11. 2024 18:00"
# # Doplň kód do uvozovek
# zacatek_lekce = datetime.strptime("7. 11. 2024, 18:00", "%d. %m. %Y, %H:%M")
# print(zacatek_lekce)                #"%d. %m. %Y, %H:%M"

#Co je potřeba doplnit do funkce time_to_christmas, aby spočítala zbývající čas do rozbalování vánočních dárků, tj. do 24. prosince 2024 18:00?
from datetime import datetime

def time_to_christmas():
    return datetime(2024, 12, 24, 18, 0) - datetime.now()

print(time_to_christmas())
