import json
import requests

hledany_nazev = input("Zadejte název nebo část názvu hledaného subjektu: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = json.dumps({"obchodniJmeno": hledany_nazev})
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)

response_data = res.json()

pocet_celkem = response_data.get("pocetCelkem", 0)
print(f"Počet nalezených subjektů: {pocet_celkem}")

ekonomicke_subjekty = response_data.get("ekonomickeSubjekty", [])
if ekonomicke_subjekty:
    for subjekt in ekonomicke_subjekty:
        obchodni_jmeno = subjekt.get("obchodniJmeno")
        ico = subjekt.get("ico")
        print(f"{obchodni_jmeno}, {ico}")
else:
    print("Nebyly nalezeny žádné subjekty.")

