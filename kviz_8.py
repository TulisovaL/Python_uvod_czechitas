# vedouci_smeny = [
#     ["pondělí", "ranní", "Pavel"],
#     ["pondělí", "odpolední", "Markéta"],
#     ["úterý", "ranní", "Míša"],
#     ["úterý", "odpolední", "Vašek"],
# ]
# for radek in vedouci_smeny:
#     den, smena, vedouci = radek #odpoved
#     print(f"V {den} vede {smena} směnu {vedouci}.")

#Proč program nic nezapíše?
#Vyber 2 odpovědi.          #na konci řádku s.. + chybí nastavení módu pro zápis (nejisté)

# vedouci_smeny = [
#     ["pondělí", "ranní", "Pavel"],
#     ["pondělí", "odpolední", "Markéta"],
#     ["úterý", "ranní", "Míša"],
#     ["úterý", "odpolední", "Vašek"],
# ]
# with open ("vedouci.txt", encoding="utf-8"):
#     for radek in vedouci_smeny:
#         radek = ",".join(radek)
#         print(radek, file=file)

#jak bude delka nabizených seznamů          #seznam_1 4, seznam_2 2, seznam_3 1

jazyky = "Python\tJava SQL\tJavascript"

seznam_1 = jazyky.split()
seznam_2 = jazyky.split(" ")
seznam_3 = jazyky.split("\t ")

print(seznam_1)
print(seznam_2)
print(seznam_3)

#jaky je typ promenné tri_musketyri = seznam retezcu (první otázka)

