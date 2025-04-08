import json
import requests

# Uživatelský vstup pro hledání
hledany_nazev = input("Zadejte název nebo část názvu hledaného subjektu: ")

# Nastavení hlaviček pro požadavek
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

# Příprava dat pro POST požadavek s uživatelským názvem
data = json.dumps({"obchodniJmeno": hledany_nazev})

# Posílání POST požadavku na API ARES
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)

# Kontrola, zda požadavek probíhl úspěšně
if res.status_code == 200:
    # Pokud je odpověď ve formátu JSON, získání dat
    response_data = res.json()

    # Zkontroluj, zda odpověď obsahuje seznam subjektů
    if "subjekty" in response_data:
        subjekty = response_data["subjekty"]
        if subjekty:
            # Pro každý subjekt v seznamu, vypíše obchodní jméno
            for subjekt in subjekty:
                obchodniJmeno = subjekt.get("obchodniJmeno", "Není k dispozici")
                print(f"Obchodní jméno: {obchodniJmeno}")
        else:
            print("Žádné subjekty nenalezeny.")
    else:
        print("Odpověď neobsahuje seznam subjektů.")
else:
    print(f"Chyba při získávání dat, status kód: {res.status_code}")