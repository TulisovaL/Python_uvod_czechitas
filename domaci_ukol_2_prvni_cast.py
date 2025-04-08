import requests
import json

hledane_ico = input("Zadejte IČO hledaného subjektu: ")

response = requests.get(f'https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{hledane_ico}')
data = response.json()

sidlo = data['sidlo']
nazevUlice = sidlo['nazevUlice']
cisloDomovni = sidlo['cisloDomovni']
nazevCastiObce = sidlo['nazevCastiObce']
psc = sidlo['psc']
nazevObce = sidlo['nazevObce']

if 'ico' in data and 'obchodniJmeno' in data and 'sidlo' in data:
    print(f"IČO: {data['ico']}")
    print(f"Název subjektu: {data['obchodniJmeno']}")
    print(f"Adresa subjektu: {nazevUlice} {cisloDomovni}, {nazevCastiObce}, {psc} {nazevObce}")

